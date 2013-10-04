inputs.conf.spec

[rpcstart://default]
*This is how the Twitter app is configured

javapath = <value>
*This is the user's twitter username/handle

options = <value>
*This is the user's password used for logging into twitter

port = <value>
*This is the user's password used for logging into twitter

packages = <value>
*Service packages to locate services

[database://default]
*database configuration

dburl = <value>
*This is the DBURL

jdbcdriver = <value>
*This is JDBC Driver Class

user = <value>
*This is the user login account to this database

password = <value>
*Login account password

parameters = <value>
*Additional parameters if needed

[opcmeasure://default]
*This is how the measures are is configured for opc server

server = <value>
*OPC server alias that is configured in opcservers.conf.

measures = <value>
*Multiple measures use semicolon ; to separate the items.

duration = <value>
*How long the measure last.

polltime = <value>
*Frequency to poll data from measurement.

collector = <value>
*Data Collector Java Class.

writer = <value>
*file or s2s two types.

parameters = <value>
*parameters to set up a writer.
