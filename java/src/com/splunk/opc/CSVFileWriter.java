package com.splunk.opc;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Map;

public class CSVFileWriter implements Writer, AutoCloseable {
	SimpleDateFormat dt = new SimpleDateFormat("MMM d HH:mm:ss");
	FileWriter writer = null;

	public CSVFileWriter(Map<String, String> parameters) {
		String fn = parameters.get("csvfile");
		File fd = new File(fn);

		boolean header = !fd.exists();
		try {
			writer = new FileWriter(fd, true);
			if (header) {
				writer.write("Measure Time,Item Name,Value,Quality\n");
				writer.flush();
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public void write(ItemData data) {
		try {
			writer.write(String.format("%s,%s,%12.3f,%d\n",
					dt.format(data.getTime()), data.getName(), data.getValue(),
					data.getQuality()));
			writer.flush();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public void close() throws Exception {
		// TODO Auto-generated method stub
		if (writer != null)
			try {
				writer.flush();
				writer.close();
			} catch (Exception e) {
				// do nothing here.
			} finally {
				writer = null;
			}
	}
}
