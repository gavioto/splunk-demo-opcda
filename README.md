splunk-demo-opcda
=================

Before installing this app, you need to download and populate some jar libraries first:

xml parser -- http://jackson.codehaus.org/
  jackson-1.9.13.jar

utgard -- http://openscada.org/projects/utgard/
  ch.qos.logback.classic_1.0.0.jar
  ch.qos.logback.core_1.0.0.jar
  org.openscada.external.jcifs_[version].jar
  org.openscada.jinterop.core_[version].jar
  org.openscada.jinterop.deps_[version].jar
  org.openscada.opc.dcom_[version].jar
  org.openscada.opc.lib_[version].jar

jdbc drivers --
  mysql-connector-java-[version]-bin.jar

deploy them to splunk-demo-opcda/java/lib/ext

Use this blog article as the user guide if you like.

  http://blogs.splunk.com/2013/10/04/manufacturing-data-acquisition-project-splunk-demo-opcda/

database, I only tested in mysql, there are still a lot of things to do.
