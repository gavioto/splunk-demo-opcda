package com.splunk.jdbc;

import java.util.Hashtable;

public class DatabaseStore {
	Hashtable<String, Database> store = new Hashtable<String, Database>();
	private static DatabaseStore instance = null;
	
	public static synchronized DatabaseStore getInstance() {
		if (instance==null) instance = new DatabaseStore();
		return instance;
	}
	
	public void updateDatabase(String name, String dburl, String jdbcdriver, String user, String password) {
		this.store.put(name, new Database(name, dburl, jdbcdriver, user, password));
	}
	
	public void removeDatabase(String name) {
		this.store.remove(name);
	}
	
	public Database getDatabase(String name) {
		return this.store.get(name);
	}
}
