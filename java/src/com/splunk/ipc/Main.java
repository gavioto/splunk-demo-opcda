package com.splunk.ipc;

import java.io.File;

import org.apache.avro.Protocol;
import org.apache.avro.ipc.Server;
import com.splunk.rpc.ServiceResponder;

public class Main {

	static Server server = null;

	public static void main(String[] args) throws Exception {

		Runtime.getRuntime().addShutdownHook(new Thread() {
			public void run() {
				if (server != null)
					server.close();

				Runtime.getRuntime().halt(0);
			}
		});

		int port = 9999;
		Protocol PROTOCOL = null;
		if (args.length > 0) {
			port = Integer.parseInt(args[0]);
			PROTOCOL = Protocol.parse(System.in);
		} else {
			PROTOCOL = Protocol
					.parse(new File(
							"/Users/btsay/btsay.btsay-mbp15/btsay.btsay-mbp15/splunk/sandbox/btsay/pyfunc/avro/services.avpr"));
		}

		server = new HttpServer(new ServiceResponder(PROTOCOL), port);
		server.start();
	}
}
