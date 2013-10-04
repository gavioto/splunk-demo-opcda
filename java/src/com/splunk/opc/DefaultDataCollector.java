package com.splunk.opc;

import org.jinterop.dcom.common.JIException;
import org.openscada.opc.lib.da.Item;
import org.openscada.opc.lib.da.ItemState;

public class DefaultDataCollector implements DataCollector {
	Writer writer;

	public DefaultDataCollector(Writer writer) {
		this.writer = writer;
	}

	@Override
	public void changed(Item item, ItemState itemState) {
		ItemData data = collect(item, itemState);
		writer.write(data);
	}

	public ItemData collect(Item item, ItemState itemState) {
		try {
			return new ItemData(item, itemState);
		} catch (JIException e) {
			return null;
		}
	}

}
