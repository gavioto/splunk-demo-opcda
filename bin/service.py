import json,os
import avro.ipc as ipc
import avro.protocol as protocol
import utils
logger = utils.setup_logging("service")

class Protocol(object):
    support_types = dict(doubleArray=dict(type="array", items="double"),
                         stringArray=dict(type="array", items="string"),
                         stringMap=dict(type="map", values="string"),
                         boolean="boolean",
                         double="double",
                         string="string",
                         int="int")

    def __init__(self):
        self.protocol = dict(namespace="com.splunk.rpc", protocol="SPLUNK_RPC", messages=dict())
         
    def dumps (self):
        return json.dumps(self.protocol)

    def add (self, schema):
        self.protocol["messages"].update(schema)

    def remove (self, service, method):
        msg = "%s#%s" % (method, service)
        if self.protocol["messages"].has_key(msg):
            del self.protocol["messages"][msg]
        

def avro_schema(schema):

    def decorator(f):
        def load_protocol():
            avpr = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir), "avro/services.avpr")
            return protocol.parse(open(avpr).read())
        
        def load_server_addr(argv, sessionKey):
            import splunk.entity as en
            ent = en.getEntity("/configs/conf-inputs", "rpcstart://default", sessionKey=sessionKey)
            logger.debug("ent=%s" %ent)
            
            return ("localhost", 9998)
        
        def avro_decorated(*args, **argv):
            # find the rpc port from inputs config.
            port = 9998
            
            if hasattr(avro_decorated, "_sessionKey_"):
                import splunk.entity as en
                ent = en.getEntity("/configs/conf-inputs", "rpcstart://default", namespace="splunk-demo-opcda", sessionKey=avro_decorated._sessionKey_, owner="nobody")
                port = ent["port"]
                logger.debug("ent=%s" %ent)
            
            server_addr = ("localhost", port)
            # server_addr = load_server_addr(argv, f._sessionKey_)
            client = ipc.HTTPTransceiver(server_addr[0], server_addr[1])

            requestor = ipc.Requestor(load_protocol(), client)
            
            def call(*argus):
                sn, val = schema.items()[0]
                
                params = {}
                reqs = val["request"]
                for i in range(len(reqs)):
                    k = reqs[i]["name"]
                    if len(argus) > i:
                        params[k] = argus[i]
                        
                logger.debug("sn=%s, parameters = %s" % (sn, params))
                
                ret = requestor.request(sn , params)

                return ret 
            
            avro_decorated.call = call
            avro_decorated.__name__ = f.__name__
            
            return f(*args, **argv)
        
        avro_decorated._schema_ = schema
            
        return avro_decorated
  
    return decorator

