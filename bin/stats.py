from service import avro_schema
import utils
logger = utils.setup_logging("stats")

@avro_schema({"covariance#com.splunk.rpc.Covariance" : 
             dict(request=[dict(name="xArray", type=dict(type="array", items="double")), 
                           dict(name="yArray", type=dict(type="array", items="double")),
                           dict(name="biasCorrected", type="boolean")],
                  response="double")})
def covariance(xArray,yArray,biasCorrected):
    logger.debug("Starting Covariance...")
    bias = True if biasCorrected==1.0 else False
    xa = [float(x) for x in xArray]
    ya = [float(y) for y in yArray] 
    
    try:
        ret = covariance.call(xa, ya, bias)
    except Exception as ex:
        logger.critical("covariance.call ex=%s" % ex)
        
    return ret


'''
xArray = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.2]
yArray = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
biasCorrected = True

print covariance(xArray=xArray,yArray=yArray,biasCorrected=biasCorrected)



{"namespace": "com.splunk.rpc",
 "protocol": "SPLUNK_RPC",
 "messages": {
     "covariance#com.splunk.rpc.Covariance": {
         "request": [{"name": "xArray", "type": {"type":"array", "items":"double"}},
                    {"name": "yArray", "type": {"type":"array", "items":"double"}},
                    {"name": "biasCorrected", "type": "boolean"}],
         "response": "double"
     }
 }
}


support_types = dict(doubleArray=dict(type="array", items="double"),
                     boolean="boolean")

message = dict(namespace="com.splunk.rpc", protocol="SPLUNK_RPC", messages=dict())
req = [dict(name=n, type= support_types[v]) for n, v in covariance._avro_["arguments"]]

resp = covariance._avro_["return_type"]

message["messages"].update({"%s#%s" % (covariance._avro_["method"], covariance._avro_["service"]) : dict (request=req, response=resp)})

print message

import json
print json.dumps(message)

'''


