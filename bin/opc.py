from service import avro_schema
import utils
logger = utils.setup_logging("opc")

@avro_schema({"runMeasure#com.splunk.opc.Test" :
              dict(request=[dict(name="server", type= dict(type="map", values="string")), 
                            dict(name="items", type= dict(type="map", values="string"))],
                   response="int")
              })
def runMeasure(server, items):
    return runMeasure.call(server, items)
