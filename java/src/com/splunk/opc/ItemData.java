package com.splunk.opc;

import java.util.Calendar;
import java.util.Date;

import org.jinterop.dcom.common.JIException;
import org.openscada.opc.lib.da.Item;
import org.openscada.opc.lib.da.ItemState;

public class ItemData {
	Double value;
	String name;
	Short quality;
	Date now;

	public ItemData(Item item, ItemState state) throws JIException {
		now = Calendar.getInstance().getTime();
		value = state.getValue().getObjectAsDouble();
		quality = state.getQuality();
		name = item.getId();
	}

	public Date getTime() {
		return now;
	}

	public Double getValue() {
		return value;
	}

	public String getName() {
		return name;
	}

	public Short getQuality() {
		return quality;
	}
}
