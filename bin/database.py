import sys, os
import xml.dom.minidom
import utils

logger = utils.setup_logging("database")

SCHEME = """<scheme>
    <title>Database Configuration</title>
    <description>Setup database connection.</description>
    <use_external_validation>true</use_external_validation>
    <streaming_mode>xml</streaming_mode>

    <endpoint>
        <args>
            <arg name="name">
                <title>Database Name</title>
                <description>The name to be used for this database configuration
                </description>
            </arg>

            <arg name="dburl">
                <title>Database Url</title>
                <description>MySQL example is: "jdbc:mysql://myhost.com/sakila".</description>
            </arg>
            
            <arg name="jdbcdriver">
                <title>JDBC Driver Java Class</title>
                <description>MySQL example is: "com.mysql.jdbc.Driver"</description>
            </arg>

            <arg name="user">
                <title>Database Access Account</title>
            </arg>

            <arg name="password">
                <title>Account Password</title>
            </arg>

            <arg name="parameters">
                <title>Extra parameters</title>
                <description>In name value pairs with semicolons, like "timeout=10;auto-committed=true".</description>
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

import jdbc

def run():
    logger.debug("start running.")
    config = get_config()
    logger.debug("config = %s" % config)
    name = config["name"].replace("database://", "")

    jdbc.updateDatabase(name, config["dburl"], config["jdbcdriver"], config["user"], config["password"], config["parameters"])
    

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
