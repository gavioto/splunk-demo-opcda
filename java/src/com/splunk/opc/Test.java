package com.splunk.opc;

import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;

import org.jinterop.dcom.common.JIException;
import org.openscada.opc.lib.common.ConnectionInformation;
import org.openscada.opc.lib.da.AccessBase;
import org.openscada.opc.lib.da.Server;
import org.openscada.opc.lib.da.SyncAccess;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.splunk.common.Factory;
import com.splunk.common.FactoryUtils;

public class Test implements AutoCloseable {
	private static Logger logger = LoggerFactory.getLogger(Test.class);

	Map<String, Factory> writerFactories = new HashMap<String, Factory>();
	Map<String, Factory> collectorFactories = new HashMap<String, Factory>();
	ScheduledExecutorService es;

	public Test() {
		es = Executors.newScheduledThreadPool(50);
	}

	protected Map<String, String> getParameterMap(String params) {
		Map<String, String> pmap = new HashMap<String, String>();

		if (params != null) {
			StringTokenizer paramTokenizer = new StringTokenizer(params, ";");
			while (paramTokenizer.hasMoreTokens()) {
				String param = paramTokenizer.nextToken();
				int eqidx = param.indexOf('=');
				if (eqidx > 0)
					pmap.put(param.substring(0, eqidx).trim(),
							param.substring(eqidx + 1).trim());
			}
		}

		return pmap;
	}

	public Integer runMeasure(Map<String, String> opcserver,
			Map<String, String> items) {

		try {
			processMeasure(new Measure(opcserver, items));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			return -1;
		}

		return 0;
	}

	public void processMeasure(Measure measure) throws Exception {
		Map<String, String> opcserver = measure.getOpcServer();
		Map<String, String> items = measure.getItems();

		ConnectionInformation ci = new ConnectionInformation();
		ci.setHost(opcserver.get("dcomhost"));
		ci.setDomain(opcserver.get("domain"));
		ci.setUser(opcserver.get("user"));
		ci.setPassword(opcserver.get("password"));
		ci.setProgId(opcserver.get("progid"));
		ci.setClsid(opcserver.get("clsid"));

		// create a new server
		Server server = new Server(ci, es);
		StringTokenizer tokenizer = new StringTokenizer(items.get("items"), ";");
		int polltime = Integer.parseInt(items.get("polltime"));
		int duration = Integer.parseInt(items.get("duration"));
		String wrclass = items.get("writer");
		String colclass = items.get("collector");

		if (!writerFactories.containsKey(wrclass)) {
			writerFactories.put(wrclass, FactoryUtils.instantiateFactory(
					Class.forName(wrclass), Map.class));
		}

		Map<String, String> params = this.getParameterMap(items
				.get("parameters"));

		Writer writer = (Writer) writerFactories.get(wrclass).create(params);

		if (!collectorFactories.containsKey(colclass)) {
			collectorFactories.put(colclass, FactoryUtils.instantiateFactory(
					Class.forName(colclass), new Class[] { Writer.class }));
		}

		DataCollector collector = (DataCollector) collectorFactories.get(
				colclass).create(writer);

		// connect to server
		server.connect();
		// add sync access, poll every 500 ms

		AccessBase access = new SyncAccess(server, polltime);

		while (tokenizer.hasMoreTokens()) {
			access.addItem(tokenizer.nextToken(), collector);
		}

		// start reading
		access.bind();
		// wait a little bit
		Thread.sleep(duration);
		// stop reading
		access.unbind();
		server.disconnect();

	}

	public static void main(String[] args) throws Exception {
		Test t = new Test();
		HashMap<String, String> server = new HashMap<String, String>();

		String host = "192.168.77.128";
		String domain = "BTSAY-VM";
		String user = "btsay";
		String password = "Passw0rd@90";
		String progid = "Matrikon.OPC.Simulation.1";
		String clsid = "F8582CF2-88FB-11D0-B850-00C0F0104305";

		server.put("dcomhost", host);
		server.put("domain", domain);
		server.put("user", user);
		server.put("password", password);
		server.put("progid", progid);
		server.put("clsid", clsid);

		HashMap<String, String> items = new HashMap<String, String>();

		String measure = "Random.Real8;Triangle Waves.Real8";
		String writer = "com.splunk.opc.CSVFileWriter";
		String collector = "com.splunk.opc.DefaultDataCollector";
		int duration = 40000;
		int polltime = 500;

		items.put("items", measure);
		items.put("writer", writer);
		items.put("collector", collector);
		items.put("duration", String.valueOf(duration));
		items.put("polltime", String.valueOf(polltime));
		items.put("parameters",
				"csvfile=/Applications/Splunk/etc/apps/splunk-demo-opcda/lookups/opc.csv");

		t.runMeasure(server, items);
		System.out
				.println("===========================================================\n\n\n\n");

		items.put("writer", "com.splunk.opc.StdoutWriter");
		items.put("duration", String.valueOf(100000));

		t.runMeasure(server, items);
	}

	@Override
	public void close() throws Exception {
		if (es != null) {
			es.shutdown();
			es = null;
		}

	}
}
