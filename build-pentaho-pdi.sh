#!/bin/sh
version="4.2.1"
if [ ! -f SOURCES/pdi-ce-$version-stable.tar.gz ];
then
    wget "http://sourceforge.net/projects/pentaho/files/Data%20Integration/$version-stable/pdi-ce-$version-stable.tar.gz" -O SOURCES/pdi-ce-$version-stable.tar.gz
fi
if [ ! -f SOURCES/ojdbc14.jar ];
then
    wget http://10.0.50.18/jdbc/ojdbc14.jar -O SOURCES/ojdbc14.jar
fi
if [ ! -f SOURCES/orai18n.jar ];
then
    wget http://10.0.50.18/jdbc/orai18n.jar -O SOURCES/orai18n.jar
fi
if [ ! -f SOURCES/postgresql-9.0-802.jdbc4.jar ];
then
    wget http://10.0.50.18/jdbc/postgresql-9.0-802.jdbc4.jar -O SOURCES/postgresql-9.0-802.jdbc4.jar
fi
if [ ! -f SOURCES/sqlitejdbc-v037-nested.jar ];
then
    wget http://10.0.50.18/jdbc/sqlitejdbc-v037-nested.jar -O SOURCES/sqlitejdbc-v037-nested.jar
fi
rm -rf BUILD SRPMS tmp || true
mkdir -p BUILD RPMS SRPMS
rpmbuild -ba --define="_topdir $PWD" --define="_tmppath $PWD/tmp" --define="ver $version" pentaho-pdi.spec
