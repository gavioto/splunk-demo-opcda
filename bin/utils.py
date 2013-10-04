import os 
import xml.dom.minidom
import logging.handlers

def setup_logging(app):
    LOG_FILENAME = os.path.join(os.environ.get('SPLUNK_HOME'), 'var','log','splunk','%s.log' % app)
    logger = logging.getLogger(app)
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1024000, backupCount=5)
    handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    return logger

logger = setup_logging("utils")

# read XML configuration passed from splunkd
def get_config(config_str):
    config = {}

    try:
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
                            config[param_name] = data

        if not config:
            raise Exception, "Invalid configuration received from Splunk."

    except Exception, e:
        raise Exception, "Error getting Splunk configuration via STDIN: %s" % str(e)

    return config

