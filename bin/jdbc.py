from service import avro_schema
import utils
logger = utils.setup_logging("jdbc")

@avro_schema({"execute#com.splunk.jdbc.SQLRunner" : 
                {"request" : [ {"name" : "database", "type": "string"}, {"name" : "statement", "type" : "string"}, 
                              {"name" : "arguments", "type" : [{"type":"array", "items":"string"}, "null"]}],
                 "response" : dict(type="array", items=dict(type="map", values="string"))}
              })
def runSQL(database, statement, **arguments):
    return runSQL.call(database, statement, **arguments)
    
@avro_schema({"updateDatabase#com.splunk.jdbc.SQLRunner" : 
                {"request" : [ {"name" : "name", "type": "string"}, {"name" : "dburl", "type" : "string"}, 
                               {"name" : "jdbcdriver", "type": "string"}, {"name" : "user", "type" : "string"}, 
                               {"name" : "password", "type": "string"}, {"name" : "parameters", "type" : "string"}],
                 "response" : "null"}
              })
def updateDatabase(name, dburl, jdbcdriver, user, password, parameters):
    updateDatabase.call(name, dburl, jdbcdriver, user, password, parameters)
    
    

    