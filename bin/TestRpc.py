import os.path as ospath
import os
import avro.ipc as ipc
import avro.protocol as protocol

PROTOCOL = protocol.parse(open(ospath.join(ospath.join(ospath.dirname(ospath.realpath(__file__)), os.pardir), "avro/services.avpr")).read())

server_addr = ('localhost', 9998)

class UsageError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def test2():
    client = ipc.HTTPTransceiver(server_addr[0], server_addr[1])
    requestor = ipc.Requestor(PROTOCOL, client)

    params = dict(x=1.0)
    try:
        msg = requestor.request('runOPCDA#com.splunk.opc.Test', params)
    except Exception as ex:
        print ex
        
    print("OK Result %s" % msg)

def test1():
    client = ipc.HTTPTransceiver(server_addr[0], server_addr[1])
    requestor = ipc.Requestor(PROTOCOL, client)

    xArray = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.2]
    yArray = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    biasCorrected = True
    
    params = dict()
    params['xArray'] = xArray
    params['yArray'] = yArray
    params['biasCorrected'] = biasCorrected
    
    msg = requestor.request('covariance#com.splunk.rpc.Covariance', params)
    
    print("Result: %s" % msg)

    # cleanup
    client.close()
    
import stats    
    
def test3():
    xArray = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.2]
    yArray = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    biasCorrected = True
    cov = stats.covariance(xArray, yArray, biasCorrected)
    print "%s" % cov
    
import opc    
def test4():
    dcomhost = "192.168.77.128"
    domain = "BTSAY-VM"
    user = "btsay"
    password = "Passw0rd@90"
    progid = "Matrikon.OPC.Simulation.1"
    clsid = "F8582CF2-88FB-11D0-B850-00C0F0104305"
    measure = "Random.Real8"
    duration = 100000
    try:
        x = opc.runMeasure(dcomhost, domain, user, password, progid, clsid, measure, duration)
        print "return = %s\n" % x
    except Exception as ex:
        print "%s\n" % ex

import jdbc
def test5():
    cov = jdbc.runSQL("mydb", "select * from actor")
    print "%s" % cov


def test6():
    name = "mydb"
    jdbcdriver = "com.mysql.jdbc.Driver"
    dburl = "jdbc:mysql://btsay-mbp15.local/sakila"
    user = "dbconnect"
    password = "Passw0rd90"
    parameters = "  "
    
    cov = jdbc.updateDatabase(name, dburl, jdbcdriver, user, password, parameters)
    print "%s" % cov


if __name__ == '__main__':
    # client code - attach to the server and send a message
    # find_services("myservs")
    test6()
    test5()
    # test2()
