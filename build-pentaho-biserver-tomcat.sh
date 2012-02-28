#!/bin/sh
version="3.10.0"
if [ ! -f SOURCES/biserver-ce-3.10.0-stable.tar.gz ];
then
    wget "http://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/$version-stable/biserver-ce-$version-stable.tar.gz" -O SOURCES/biserver-ce-$version-stable.tar.gz
fi
if [ ! -f SOURCES/mysql-connector-java-3.1.14-bin.jar ];
then
    wget http://10.0.50.18/jdbc/mysql-connector-java-3.1.14-bin.jar -O SOURCES/mysql-connector-java-3.1.14-bin.jar
fi
if [ ! -f SOURCES/ojdbc14.jar ];
then
    wget http://10.0.50.18/jdbc/ojdbc14.jar -O SOURCES/ojdbc14.jar
fi
if [ ! -f SOURCES/orai18n.jar ];
then
    wget http://10.0.50.18/jdbc/orai18n.jar -O SOURCES/orai18n.jar
fi
if [ ! -f SOURCES/postgresql-9.0-802.jdbc3.jar ];
then
    wget http://10.0.50.18/jdbc/postgresql-9.0-802.jdbc3.jar -O SOURCES/postgresql-9.0-802.jdbc3.jar
fi
if [ ! -f SOURCES/sqlitejdbc-v037-nested.jar ];
then
    wget http://10.0.50.18/jdbc/sqlitejdbc-v037-nested.jar -O SOURCES/sqlitejdbc-v037-nested.jar
fi
rm -rf BUILD RPMS SRPMS tmp || true
mkdir -p BUILD RPMS SRPMS
rpmbuild -ba --define="_topdir $PWD" --define="_tmppath $PWD/tmp" --define="ver $version" pentaho-biserver-tomcat.spec
