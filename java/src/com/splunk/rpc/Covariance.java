package com.splunk.rpc;

public class Covariance {
	org.apache.commons.math3.stat.correlation.Covariance covariance;

	public Covariance() {
		covariance = new org.apache.commons.math3.stat.correlation.Covariance();
	}

	public Double covariance(Double[] xArray, Double[] yArray,
			Boolean biasCorrected) {
		double[] xa = convert(xArray);
		double[] ya = convert(yArray);
		boolean bc = biasCorrected.booleanValue();

		return covariance.covariance(xa, ya, bc);
	}

	protected double[] convert(Double[] array) {
		double[] xa = new double[array.length];

		int i = 0;
		for (Double d : array) {
			xa[i] = d.doubleValue();
			++i;
		}

		return xa;
	}
}
