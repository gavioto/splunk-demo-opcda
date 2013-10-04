package com.splunk.opc;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.HashMap;
import java.util.Map;

import org.codehaus.jackson.JsonGenerationException;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectMapper;

public class JsonFileWriter implements Writer, AutoCloseable {
	SimpleDateFormat dt = new SimpleDateFormat("MMM d HH:mm:ss");
	ByteArrayOutputStream cache = new ByteArrayOutputStream(1024);
	FileWriter writer = null;
	public JsonFileWriter(Map<String, String> parameters) throws IOException {
		String fn = parameters.get("jsonfile");
		writer = new FileWriter(fn);
	}

	@Override
	public void write(ItemData data) {
		ObjectMapper mapper = new ObjectMapper();
		Map<String,Object> userData = new HashMap<String,Object>();
		Map<String,String> dataStruct = new HashMap<String,String>();
		dataStruct.put("timestamp", dt.format(data.getTime()));
		dataStruct.put("value", String.format("%12.3f", data.getValue()));
		dataStruct.put("data_quality", String.format("%d", data.getQuality()));
		userData.put("item", data.getName());
		userData.put("measure", dataStruct);
		try {
			cache.reset();
			mapper.writeValue(cache, userData);
			writer.write(String.format("%s\n", cache.toString()));
			writer.flush();
		} catch (JsonGenerationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (JsonMappingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}		
	}

	@Override
	public void close() throws Exception {
		writer.close();
	}
}
