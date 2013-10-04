package com.splunk.opc;

import java.io.IOException;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.util.Date;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class S2S {

	public byte[] encodeEvent(String source, String sourcetype, String host,
			String raw, boolean encode_sig) {
		byte[] encodedSig = encode_sig ? this.encode_sig() : null;
		byte[] encodedSource = this.encodeSource(source);
		byte[] encodedSourceType = this.encodeSourceType(sourcetype);
		byte[] encodedHost = this.encodeHost(host);
		byte[] encodedRaw = raw != null ? this.encodeRaw(raw) : this
				.encodeDone();
		byte[] encodedTrailerRaw = this.encodeString("_raw");

		int sizeSerializedPD = 4 + encodedSource.length
				+ encodedSourceType.length + encodedHost.length
				+ encodedRaw.length + 4 + encodedTrailerRaw.length;

		ByteBuffer buffer = ByteBuffer.allocate(4
				+ (encodedSig != null ? encodedSig.length : 0)
				+ sizeSerializedPD);
		if (encode_sig)
			buffer.put(encodedSig);
		buffer.putInt(sizeSerializedPD).putInt(4);
		buffer.put(encodedSource).put(encodedSourceType).put(encodedHost)
				.put(encodedRaw);
		buffer.putInt(0).put(encodedTrailerRaw);

		return buffer.array();
	}

	public byte[] encode_sig() {
		byte[] _signature = ByteBuffer.allocate(128)
				.put("--splunk-cooked-mode-v2--".getBytes()).array();
		byte[] _serverName = ByteBuffer.allocate(256).put("s2s-api".getBytes())
				.array();
		byte[] _mgmtPort = ByteBuffer.allocate(16).put("0".getBytes()).array();

		return ByteBuffer.allocate(128 + 256 + 16).put(_signature)
				.put(_serverName).put(_mgmtPort).array();
	}

	public byte[] encode_32(int val) {
		return ByteBuffer.allocate(5).putInt(1695609641).put((byte) 0).array();
	}

	public byte[] encodeString(String str) {
		// size+1:str:\0
		byte[] bytes = str.getBytes();
		return ByteBuffer.allocate(bytes.length + 5).putInt(str.length() + 1)
				.put(bytes).put((byte) 0).array();
	}

	public byte[] encodeKeyValue(String key, String value) {
		byte[] kb = encodeString(key);
		byte[] vb = encodeString(value);
		return ByteBuffer.allocate(kb.length + vb.length).put(kb).put(vb)
				.array();
	}

	public byte[] encodeSource(String source) {
		return encodeKeyValue("MetaData:Source", source);
	}

	public byte[] encodeSourceType(String sourceType) {
		return encodeKeyValue("MetaData:Sourcetype", sourceType);
	}

	public byte[] encodeHost(String host) {
		return encodeKeyValue("MetaData:Host", host);
	}

	public byte[] encodeRaw(String raw) {
		return encodeKeyValue("_raw", raw);
	}

	public byte[] encodeDone() {
		return encodeKeyValue("_done", "_done");
	}

	// test purpose

	static class Test {
		int eventId = 0;
		SimpleDateFormat dt = new SimpleDateFormat("MMM d HH:mm:ss");

		public String get_event() {
			eventId += 1;
			if (eventId < 100) {
				Date now = Calendar.getInstance().getTime();
				return String
						.format("%s busybox SecurityAgent[103]: Login failed eventid=%d\n",
								dt.format(now), eventId);
			}
			return null;
		}

		public void sendEvents(S2S s, Socket socket) throws IOException {
			String source = "source::mysource";
			String sourceType = "sourcetype::mysourcetype";
			String host = "host::myhost";
			String event = null;

			boolean encode_sig = true;
			while ((event = get_event()) != null) {
				byte[] evt = s.encodeEvent(source, sourceType, host, event,
						encode_sig);
				socket.getOutputStream().write(evt);
				encode_sig = false;
			}
		}

	};

	public static void main(String[] args) {
		S2S s = new S2S();

		Socket socket;
		try {
			socket = new Socket("localhost", 19999);

			Test t = new Test();
			t.sendEvents(s, socket);
		} catch (IOException e) {
			System.out.println(e);
		}
	}
}
