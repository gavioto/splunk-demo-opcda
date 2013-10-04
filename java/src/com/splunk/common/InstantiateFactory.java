package com.splunk.common;

import java.io.Serializable;
import java.lang.reflect.Constructor;

@SuppressWarnings("serial")
public class InstantiateFactory implements Factory, Serializable {
	/** The class to create */
	private final Class iClassToInstantiate;
	/** The constructor parameter types */
	private final Class[] iParamTypes;
	/** The constructor arguments */
	private final Object[] iArgs;
	/** The constructor */
	private transient Constructor iConstructor = null;

	public static Factory getInstance(Class classToInstantiate,
			Class[] paramTypes, Object[] args) {
		assert (classToInstantiate != null);

		if (paramTypes == null || paramTypes.length == 0) {
			return new InstantiateFactory(classToInstantiate);
		} else {
			paramTypes = (Class[]) paramTypes.clone();
			if (args != null)
				args = (Object[]) args.clone();
			return new InstantiateFactory(classToInstantiate, paramTypes, args);
		}
	}

	public InstantiateFactory(Class classToInstantiate) {
		super();
		iClassToInstantiate = classToInstantiate;
		iParamTypes = null;
		iArgs = null;
		findConstructor();
	}

	@SuppressWarnings("rawtypes")
	public InstantiateFactory(Class classToInstantiate, Class[] paramTypes,
			Object[] args) {
		super();
		iClassToInstantiate = classToInstantiate;
		iParamTypes = paramTypes;
		iArgs = args;
		findConstructor();
	}

	@SuppressWarnings({ "unchecked" })
	private void findConstructor() {
		try {
			iConstructor = iClassToInstantiate.getConstructor(iParamTypes);
		} catch (NoSuchMethodException ex) {
			throw new IllegalArgumentException(
					"InstantiateFactory: The constructor must exist and be public ");
		}
	}

	@Override
	public Object create() throws Exception {
		// needed for post-serialization
		if (iConstructor == null) {
			findConstructor();
		}
		return iConstructor.newInstance(iArgs);
	}

	@Override
	public Object create(Object... args) throws Exception {
		if (iConstructor == null) {
			findConstructor();
		}
		return iConstructor.newInstance(args);
	}

}
