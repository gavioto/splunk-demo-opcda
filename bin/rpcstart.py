import sys, os
import xml.dom.minidom
import subprocess
import signal, utils
import splunk.entity as en
from service import Protocol

logger = utils.setup_logging("rpcstart")

SCHEME = """<scheme>
    <title>Splunk RPC Startup</title>
    <description>Start up RPC service server.</description>
    <use_external_validation>true</use_external_validation>
    <streaming_mode>xml</streaming_mode>

    <endpoint>
        <args>
            <arg name="name">
                <title>Resource name</title>
                <description> Java RPC server name
                </description>
            </arg>

            <arg name="javapath">
                <title>Java Installation</title>
            </arg>

            <arg name="options">
                <title>Java Options</title>
            </arg>

            <arg name="port">
                <title>RPC Server Port</title>
                <data_type>number</data_type>
            </arg>

            <arg name="packages">
                <title>Service Packages</title>
            </arg>
            
        </args>
    </endpoint>
</scheme>
"""

def validate_conf(config, key):
    if key not in config:
        raise Exception, "Invalid configuration received from Splunk: key '%s' is missing." % key

# read XML configuration passed from splunkd
def get_config():
    config_str = sys.stdin.read()
    return utils.get_config(config_str)

def get_classpath_script():
    curr = os.path.dirname(os.path.realpath(__file__))
    libpath = os.path.join(os.path.join(curr, os.pardir), "java/lib")

    jars = []        
    for dirpath, dirnames, filenames in os.walk(libpath):
        for filename in [f for f in filenames if f.endswith(".jar")]:
            jars.append(os.path.join(dirpath, filename))
            
    if "ext" in dirnames:
        for ext_dirpath, ext_dirnames, ext_filenames in os.walk(os.path.join(dirpath, "ext")):
            for filename in [f for f in ext_filenames if f.endswith(".jar")]:
                jars.append(os.path.join(ext_dirpath, filename))
            
            
    return ':'.join(jars)

import importlib,inspect

def find_services(pkg):
    module = importlib.import_module(pkg)
    members = inspect.getmembers(module)
    return [f for n, f in members if inspect.isfunction(f) and hasattr(f, "_schema_") and f.__name__=="avro_decorated"]
#    return [f for n, f in members if inspect.isfunction(f) and hasattr(f, "_avro_") and f.__name__=="avro_decorated"]

def initialize(config):
    module = importlib.import_module("rpcinits")
    members = inspect.getmembers(module)
    for fn in [f for n, f in members if inspect.isfunction(f)]:
        fn(config)


def service_avpr():
    curr = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(os.path.join(curr, os.pardir), "avro/services.avpr")

def server_log():
    home = os.environ.get("SPLUNK_HOME", ".")
    
    return os.path.join(home, "var/log/splunk/rpcserver.log")

def update_protocol_avpr(packages):
    protocol = Protocol()

    for pkg in packages:
        funcs = find_services(pkg)
        for f in funcs:
            protocol.add(f._schema_)
            
    p = protocol.dumps()

    fd = open (service_avpr(), "w")
    fd.write("%s" % p)
    fd.flush()
    fd.close()

    return p

import time
def run():
#    java = "/Library/Java/JavaVirtualMachines/1.7.0.jdk/Contents/Home/bin/java"
    logger.debug("start running.")
    
    config = get_config()
    name = config["name"]
    
    if name!="rpcstart://default":
        logger.critical("Only one RPC server the default, can start up. This is not the default name = %s." % name)
        raise Exception("Only one RPC server can start up!")
        sys.exit(-1)
    
    java = config["javapath"]
    port = config["port"]
    options = config["options"]
    packages = config["packages"].split(";")

    try:
        p = update_protocol_avpr(packages)
        jcmd = '%s %s -classpath %s com.splunk.ipc.Main %s' % (java, options, get_classpath_script(), port)
        logger.debug("protocol = %s" % p)
        
        pf = open(service_avpr(), "r")
        logger.debug("jcommand = %s" % jcmd)
        fd = open(server_log(), "a")
#        proc = subprocess.Popen(jcmd, shell=True, stdin=pf, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        proc = subprocess.Popen(jcmd, shell=True, stdin=pf, stdout=fd, stderr=fd)

        def handler(signum, frame):
            proc.send_signal(signum)

        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGABRT, handler)
        signal.signal(signal.SIGTERM, handler)
    
        logger.info("proc.pid = %s\n" % proc.pid)

        time.sleep(10)
        try:
            initialize(config)
        except Exception as ex:
            logger.critical("Initialization process failed for %s, but RPC is up." % ex)
                    
    except Exception as ex:
        logger.critical("Start RPC failed as %s" % ex)
        proc.send_signal(signal.SIGTERM)
        raise ex
    
    
    return_code = proc.wait()
    logger.info("rpc stop at return code = %s\n" % return_code)
    
    # print return_code
    

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

def usage():
    print "usage: %s [--scheme|--validate-arguments]"
    sys.exit(2)

def test():
    pass

def validate_arguments():
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
