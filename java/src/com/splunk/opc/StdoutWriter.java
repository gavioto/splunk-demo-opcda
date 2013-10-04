package com.splunk.opc;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Map;

public class StdoutWriter implements Writer {
	SimpleDateFormat dt = new SimpleDateFormat("MMM d HH:mm:ss");

	public StdoutWriter(Map<String, Object> parameters) {

	}

	@Override
	public void write(ItemData data) {
		System.out.println(String.format("%s Item=%s Value=%f8.3 Quality=%d",
				dt.format(data.getTime()), data.getName(), data.getValue(),
				data.getQuality()));
	}

}
