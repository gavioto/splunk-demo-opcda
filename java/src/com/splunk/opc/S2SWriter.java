package com.splunk.opc;

import java.io.IOException;
import java.net.Socket;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Map;

import org.codehaus.jackson.map.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class S2SWriter implements Writer, AutoCloseable {
	private static Logger logger = LoggerFactory.getLogger(S2SWriter.class);

	S2S s = new S2S();
	Socket socket;
	boolean encode_sig = true;
	SimpleDateFormat dt = new SimpleDateFormat("MMM d HH:mm:ss");

	public S2SWriter(Map<String, String> parameters) {
		try {
			socket = new Socket("localhost", 19999);
		} catch (IOException e) {
			logger.error("Cannot connect to splunk.", e);
		}
	}

	@Override
	public void write(ItemData data) {
		String source = "source::opc";
		String sourceType = "sourcetype::opcjson";
		String host = "host::opcserver";
		String event = null;
		ObjectMapper mapper = new ObjectMapper();

		try {
			event = String.format("%s %s\n", dt.format(data.getTime()),
					mapper.writeValueAsString(data));
			byte[] evt = s.encodeEvent(source, sourceType, host, event,
					encode_sig);
			socket.getOutputStream().write(evt);
			encode_sig = false;

		} catch (Exception e) {
			logger.error("Sending data to splunk failed.", e);
		}
	}

	@Override
	public void close() {
		try {
			this.socket.close();
		} catch (IOException e) {
			// do nothing, it doesn't matter if cannot close the socket.
		} finally {
			this.socket = null;
		}
	}
}
