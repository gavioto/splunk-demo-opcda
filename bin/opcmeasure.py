import sys, os
import xml.dom.minidom
import utils
import opc
import splunk.entity as en

logger = utils.setup_logging("opcmeasure")

SCHEME = """<scheme>
    <title>OPC DA Collector</title>
    <description>Setup opc measure.</description>
    <use_external_validation>true</use_external_validation>
    <streaming_mode>xml</streaming_mode>

    <endpoint>
        <args>
            <arg name="name">
                <title>OPC DA Collector</title>
                <description>OPC measure name
                </description>
            </arg>

            <arg name="server">
                <title>Opc Server</title>
                <description>Opc Server alias that is configured in opcservers.conf.</description>
            </arg>
            
            <arg name="measures">
                <title>Measure Items</title>
                <description>Separated with semicolon ; if multiple.</description>
            </arg>

            <arg name="polltime">
                <title>Poll Time</title>
                <description>Time duration to poll data.</description>
                <data_type>number</data_type>
            </arg>

            <arg name="duration">
                <title>Duration</title>
                <description>Measure duration.</description>
                <data_type>number</data_type>
            </arg>

            <arg name="collector">
                <title>Data Collector</title>
                <description>Java Class name to collect data.</description>
            </arg>

            <arg name="writer">
                <title>Data Writer</title>
                <description>Java Class to write/output the measure data in varied formats.</description>
            </arg>

            <arg name="parameters">
                <title>Data Writer initial parameters</title>
                <description>The parameters needed to initialize writer instance.</description>
            </arg>
            
        </args>
    </endpoint>
</scheme>
"""

def validate_conf(config, key):
    if key not in config:
        raise Exception, "Invalid configuration received from Splunk: key '%s' is missing." % key

def apply_env(data):
    ndata = data.lstrip("\"").rstrip("\"")
    
    env = os.environ
    tokens = ndata.split("$")
    for n in range(0, len(tokens)):
        if n%2==1:
            tokens[n] = env.get(tokens[n], "$%s$" % tokens[n])
    
    return "".join(tokens)

# read XML configuration passed from splunkd
def get_config():
    config = {}

    try:
        # read everything from stdin
        config_str = sys.stdin.read()

        # parse the config XML
        doc = xml.dom.minidom.parseString(config_str)
        
        
        server_uri = doc.getElementsByTagName("server_uri")[0]
        session_key = doc.getElementsByTagName("session_key")[0]
        config["server_uri"] = server_uri.childNodes[0].nodeValue
        config["session_key"] = session_key.childNodes[0].nodeValue
        
        root = doc.documentElement
        
        conf_node = root.getElementsByTagName("configuration")[0]
        if conf_node:
            stanza = conf_node.getElementsByTagName("stanza")[0]
            if stanza:
                stanza_name = stanza.getAttribute("name")
                if stanza_name:
                    config["name"] = stanza_name

                    params = stanza.getElementsByTagName("param")
                    for param in params:
                        param_name = param.getAttribute("name")
                        if param_name and param.firstChild and \
                           param.firstChild.nodeType == param.firstChild.TEXT_NODE:
                            data = param.firstChild.data
                            config[param_name] = apply_env(data)

        if not config:
            raise Exception, "Invalid configuration received from Splunk."

        # just some validation: make sure these keys are present (required)
        # validate_conf(config, "name")
        # validate_conf(config, "key_id")
        # validate_conf(config, "secret_key")
        # validate_conf(config, "checkpoint_dir")
    except Exception, e:
        raise Exception, "Error getting Splunk configuration via STDIN: %s" % str(e)

    return config


def service_avpr():
    curr = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(os.path.join(curr, os.pardir), "avro/services.avpr")

def run():
    logger.debug("start running.")
    config = get_config()
    logger.debug("config = %s" % config)
    try:
        servers = en.getEntities(["admin","opcservers"], sessionKey=config["session_key"], hostPath=config["server_uri"])
        logger.debug("servers = %s" % servers)
    except Exception as ex:
        logger.critical("%ss" % ex)
    
    server = servers[config["server"]]    
    logger.debug("server = %s" % server)
    
    opcserver = dict( dcomhost = server["dcomhost"], domain = server["domain"], user = server["user"], password = server["password"], 
                      progid = server["progid"], clsid = server["clsid"])
    
    measures = dict( items = config["measures"], duration = config["duration"], 
                     polltime = config["polltime"], collector = config["collector"], writer = config["writer"], parameters = config.get("parameters", ""))
    
    logger.debug("Measured server = %s." % opcserver)
    logger.debug("Measuring the items = %s." % measures)

    try:
        msg = opc.runMeasure(opcserver, measures)
        logger.debug("Measuring is done [%s]." % msg)
    except Exception as ex:
        logger.critical("Request error as ex = %s" % ex)
    

def do_scheme():
    print SCHEME

def get_validation_data():
    val_data = {}

    # read everything from stdin
    val_str = sys.stdin.read()

    # parse the validation XML
    doc = xml.dom.minidom.parseString(val_str)
    root = doc.documentElement

    item_node = root.getElementsByTagName("item")[0]
    if item_node:

        name = item_node.getAttribute("name")
        val_data["stanza"] = name

        params_node = item_node.getElementsByTagName("param")
        for param in params_node:
            name = param.getAttribute("name")
            if name and param.firstChild and \
               param.firstChild.nodeType == param.firstChild.TEXT_NODE:
                val_data[name] = param.firstChild.data

    return val_data

# make sure that the amazon credentials are good
def validate_arguments():
    pass

def usage():
    print "usage: %s [--scheme|--validate-arguments]"
    sys.exit(2)

def test():
    pass

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--scheme":
            do_scheme()
        elif sys.argv[1] == "--validate-arguments":
            validate_arguments()
        elif sys.argv[1] == "--test":
            test()
        else:
            usage()
    else:
        # just request data from S3
        run()
        
    sys.exit(0)
