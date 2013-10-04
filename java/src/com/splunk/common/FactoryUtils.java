package com.splunk.common;

public class FactoryUtils {

	public FactoryUtils() {
		super();
	}

	public static Factory instantiateFactory(Class classToInstantiate) {
		return InstantiateFactory.getInstance(classToInstantiate, null, null);
	}

	public static Factory instantiateFactory(Class classToInstantiate,
			Class... paramTypes) {
		return InstantiateFactory.getInstance(classToInstantiate, paramTypes,
				null);
	}

	public static Factory instantiateFactory(Class classToInstantiate,
			Class[] paramTypes, Object[] args) {
		return InstantiateFactory.getInstance(classToInstantiate, paramTypes,
				args);
	}

}
