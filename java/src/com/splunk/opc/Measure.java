package com.splunk.opc;

import java.util.Map;

public class Measure {
	Map<String, String> opcserver = null;
	Map<String, String> items = null;

	public Measure(Map<String, String> opcserver, Map<String, String> items) {
		this.opcserver = opcserver;
		this.items = items;
	}

	public Map<String, String> getOpcServer() {
		return this.opcserver;
	}

	public Map<String, String> getItems() {
		return this.items;
	}

}
