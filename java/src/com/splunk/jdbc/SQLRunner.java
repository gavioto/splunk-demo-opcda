package com.splunk.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ParameterMetaData;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.sql.Types;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.commons.lang3.time.DateFormatUtils;

public class SQLRunner {

	// JDBC driver name and database URL
	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
	static final String DB_URL = "jdbc:mysql://btsay-mbp15.local/sakila";

	// Database credentials
	static final String USER = "dbconnect";
	static final String PASS = "monday";

	public void setShort(PreparedStatement stmt, int column, String value)
			throws NumberFormatException, SQLException {
		stmt.setShort(column, Short.parseShort(value));
	}

	public void setBoolean(PreparedStatement stmt, int column, String value)
			throws NumberFormatException, SQLException {
		stmt.setBoolean(column, Boolean.parseBoolean(value));
	}

	public void setDouble(PreparedStatement stmt, int column, String value)
			throws NumberFormatException, SQLException {
		stmt.setDouble(column, Double.parseDouble(value));
	}

	public void setInt(PreparedStatement stmt, int column, String value)
			throws NumberFormatException, SQLException {
		stmt.setInt(column, Integer.parseInt(value));
	}

	public void setString(PreparedStatement stmt, int column, String value)
			throws SQLException {
		stmt.setString(column, value);
	}

	public void setFloat(PreparedStatement stmt, int column, String value)
			throws NumberFormatException, SQLException {
		stmt.setFloat(column, Float.parseFloat(value));
	}

	public void setLong(PreparedStatement stmt, int column, String value)
			throws NumberFormatException, SQLException {
		stmt.setLong(column, Long.parseLong(value));
	}

	public void setTimestamp(PreparedStatement stmt, int column, String value)
			throws NumberFormatException, SQLException {
		stmt.setTimestamp(column, Timestamp.valueOf(value));
	}

	public String getString(ResultSet rs, int column, int type)
			throws SQLException {
		switch (type) {
		case Types.DOUBLE:
			return Double.toString(rs.getDouble(column));
		case Types.BOOLEAN:
			return Boolean.toString(rs.getBoolean(column));
		case Types.SMALLINT:
			return Short.toString(rs.getShort(column));
		case Types.INTEGER:
			return Integer.toString(rs.getInt(column));
		case Types.VARCHAR:
		case Types.LONGNVARCHAR:
			return rs.getString(column);
		case Types.TIMESTAMP:
			return DateFormatUtils.ISO_DATETIME_FORMAT.format(rs
					.getDate(column));
		}
		return null;
	}

	public List<Map<String, String>> execute(String database, String statement,
			String... arguments) throws Exception {
		ArrayList<Map<String, String>> ret = new ArrayList<Map<String, String>>();
		Database db = DatabaseStore.getInstance().getDatabase(database);
		if (db==null) throw new Exception("Database Not Found.");
		
		Class.forName(db.getJDBCDriver());
		Connection c = DriverManager.getConnection(db.getDbURL(), db.getUser(), db.getPassword());
		PreparedStatement stmt = c.prepareStatement(statement);
		ParameterMetaData pmeta = stmt.getParameterMetaData();

		assert (pmeta.getParameterCount() == arguments.length);

		if (arguments!=null && arguments.length > 0) {
			for (int i = 1; i <= arguments.length; ++i)
				switch (pmeta.getParameterType(i)) {
				case Types.DOUBLE:
					this.setDouble(stmt, i, arguments[i]);
					break;
				case Types.BOOLEAN:
					this.setBoolean(stmt, i, arguments[i]);
					break;
				case Types.INTEGER:
					this.setInt(stmt, i, arguments[i]);
					break;
				case Types.VARCHAR:
				case Types.LONGNVARCHAR:
					this.setString(stmt, i, arguments[i]);
					break;
				case Types.TIMESTAMP:
					this.setTimestamp(stmt, i, arguments[i]);
					break;
				}
		}

		ResultSet rs = stmt.executeQuery();
		ResultSetMetaData meta = stmt.getMetaData();

		while (rs.next()) {
			Map<String, String> r = new HashMap<String, String>();
			for (int j = 1; j <= meta.getColumnCount(); ++j)
				r.put(meta.getColumnName(j),
						this.getString(rs, j, meta.getColumnType(j)));
			ret.add(r);
		}

		return ret;
	}
	
	public void updateDatabase(String name, String dburl, String jdbcdriver, String user, String password, String parameters) {
		DatabaseStore.getInstance().updateDatabase(name, dburl, jdbcdriver, user, password);
	}
	
}
