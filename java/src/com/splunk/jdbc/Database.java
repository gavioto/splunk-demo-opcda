package com.splunk.jdbc;

public class Database {
	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
	static final String DB_URL = "jdbc:mysql://btsay-mbp15.local/sakila";

	// Database credentials
	static final String USER = "dbconnect";
	static final String PASS = "monday";

	String name, dburl, jdbcdriver, user, password;
	
	public Database(String name, String dburl, String jdbcdriver, String user, String password) {
		this.name = name;
		this.dburl = dburl;
		this.jdbcdriver = jdbcdriver;
		this.user = user;
		this.password = password;
	}
	
	public String getName() {
		return this.name;
	}
	
	public String getDbURL() {
		return this.dburl;
	}
	
	public String getJDBCDriver() {
		return this.jdbcdriver;
	}
	
	public String getUser() {
		return this.user;
	}
	
	public String getPassword() {
		return this.password;
	}
}

