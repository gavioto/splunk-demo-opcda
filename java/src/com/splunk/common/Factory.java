package com.splunk.common;

public interface Factory {
	public Object create() throws Exception;

	public Object create(Object... args) throws Exception;
}
