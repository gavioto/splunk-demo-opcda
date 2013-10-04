package com.splunk.rpc;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import org.apache.avro.AvroRemoteException;
import org.apache.avro.AvroRuntimeException;
import org.apache.avro.Protocol;
import org.apache.avro.Protocol.Message;
import org.apache.avro.Schema;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.ipc.generic.GenericResponder;
import org.apache.avro.util.Utf8;
import org.apache.commons.collections.Factory;
import org.apache.commons.collections.FactoryUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ServiceResponder extends GenericResponder {
	private static Logger logger = LoggerFactory
			.getLogger(ServiceResponder.class);

	static class Argument {
		Class clazz;
		Object value;

		public Argument(Class clazz, Object value) {
			this.clazz = clazz;
			this.value = value;
		}

		public Class getClassType() {
			return clazz;
		}

		public Object getValue() {
			return value;
		}
	}

	HashMap<String, Factory> services = new HashMap<String, Factory>();

	public ServiceResponder(Protocol local) {
		super(local);

		for (String name : local.getMessages().keySet()) {
			String className = name.split("#")[1];

			if (!services.containsKey(className)) {
				try {
					services.put(className, FactoryUtils
							.instantiateFactory(Class.forName(className)));
				} catch (ClassNotFoundException e) {
					logger.error(
							String.format(
									"Cannot create a service factory for this service name %s",
									className), e);
				}
			}
		}
	}

	protected Argument convert(Object val, Schema schema) throws Exception {
		switch (schema.getType()) {
		case NULL:
			return new Argument(null, null);
		case UNION:
			Class clazz = null;
			Object value;
			for (Schema s : schema.getTypes()) {
				if (clazz == null)
					clazz = this.getClassType(s);
				try {
					value = convert(val, s);
				} catch (Exception e) {
					value = e;
				}
			}

			if (val instanceof Exception)
				throw (Exception) val;
			return new Argument(clazz, val);
		case STRING:
			if (val instanceof Utf8)
				return new Argument(this.getClassType(schema),
						((Utf8) val).toString());
		case BOOLEAN:
		case DOUBLE:
		case FLOAT:
		case INT:
		case LONG:
			return new Argument(this.getClassType(schema), val);
		case ARRAY:
			@SuppressWarnings("unchecked")
			GenericData.Array<Object> array = (GenericData.Array<Object>) val;
			Object[] values = createEmptyArray(schema.getElementType(),
					array.size());
			Iterator<Object> iter = array.iterator();
			int n = 0;
			while (iter.hasNext()) {
				values[n] = convert(iter.next(), schema.getElementType())
						.getValue();
				++n;
			}

			return new Argument(this.getClassType(schema), values);
		case MAP:
			Map<String, Object> nmap = new HashMap<String, Object>();
			Map map = (Map) val;
			Set keys = map.keySet();
			for (Object k : keys) {
				nmap.put(k.toString(), convertUtf8(map.get(k)));
			}
			return new Argument(this.getClassType(schema), nmap);
		}

		throw new Exception("Not Supported Type.");
	}

	protected Object convertUtf8(Object val) {
		return (val instanceof Utf8) ? ((Utf8) val).toString() : val;
	}

	protected Object[] createEmptyArray(Schema schema, int size) {
		switch (schema.getType()) {
		case BOOLEAN:
			return new Boolean[size];
		case STRING:
			return new String[size];
		case DOUBLE:
			return new Double[size];
		case FLOAT:
			return new Float[size];
		case INT:
			return new Integer[size];
		case LONG:
			return new Long[size];
		}
		return new Object[0];
	}

	protected Argument getFieldValueFromRecord(GenericRecord record,
			Schema.Field field) throws Exception {
		return convert(record.get(field.name()), field.schema());
	}

	protected Class getClassType(Schema schema) {
		switch (schema.getType()) {
		case NULL:
			return null;
		case BOOLEAN:
			return Boolean.class;
		case STRING:
			return String.class;
		case DOUBLE:
			return Double.class;
		case FLOAT:
			return Float.class;
		case INT:
			return Integer.class;
		case LONG:
			return Long.class;
		case MAP:
			return Map.class;
		case ARRAY:
			switch (schema.getElementType().getType()) {
			case BOOLEAN:
				return Boolean[].class;
			case STRING:
				return String[].class;
			case DOUBLE:
				return Double[].class;
			case FLOAT:
				return Float[].class;
			case INT:
				return Integer[].class;
			case LONG:
				return Long[].class;
			default:
				throw new Error("Not Supported Type.");
			}
		default:
			throw new Error("Not Supported Type.");
		}
	}

	@Override
	public Object respond(Message message, Object request) throws Exception {
		String names[] = message.getName().split("#");
		Factory factory = services.get(names[1]);
		if (factory == null)
			throw new Exception(String.format(
					"No such service class [%s] exists.", names[1]));
		Object impl = factory.create();
		int numParams = message.getRequest().getFields().size();
		Object[] params = new Object[numParams];
		Class[] paramTypes = new Class[numParams];
		GenericRecord record = (GenericRecord) request;

		int i = 0;
		try {
			for (Schema.Field param : message.getRequest().getFields()) {
				Argument arg = getFieldValueFromRecord(record, param);
				params[i] = arg.getValue();
				paramTypes[i] = arg.getClassType();
				i++;
			}

			Method method = impl.getClass().getMethod(names[0], paramTypes);
			method.setAccessible(true);
			return method.invoke(impl, params);
		} catch (InvocationTargetException e) {
			if (e.getTargetException() instanceof Exception) {
				throw new AvroRemoteException(e.getTargetException().getMessage());
			} else {
				throw new Exception(e.getTargetException().getMessage());
			}
		} catch (NoSuchMethodException e) {
			throw new AvroRuntimeException(e);
		} catch (IllegalAccessException e) {
			throw new AvroRuntimeException(e);
		}
	}
}
