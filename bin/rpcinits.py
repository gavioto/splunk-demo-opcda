
import splunk.entity as en
import jdbc, utils

logger = utils.setup_logging("rpcinits")

def load_db(config):
    ents = en.getEntities(["admin","conf-inputs"], namespace="splunk-demo-opcda", owner="nobody", sessionKey=config["session_key"], hostPath=config["server_uri"])
    # logger.debug("%s" % ents)
    for dbn, dbv in [(n, v) for n, v in ents.items() if n.startswith("database://")]:
        name = dbn.replace("database://", "")
        logger.debug("name=%s" % name)
        logger.debug("values=%s" % dbv)
        jdbc.updateDatabase(name, dbv["dburl"], dbv["jdbcdriver"], dbv["user"], dbv["password"], dbv["parameters"])
        