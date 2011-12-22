#!/bin/sh
version="3.10.0"
if [ ! -f SOURCES/biserver-ce-3.10.0-stable.tar.gz ];
then
    wget "http://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/$version-stable/biserver-ce-$version-stable.tar.gz" -O SOURCES/biserver-ce-$version-stable.tar.gz
fi
rm -rf BUILD RPMS SRPMS tmp || true
mkdir -p BUILD RPMS SRPMS
rpmbuild -ba --define="_topdir $PWD" --define="_tmppath $PWD/tmp" --define="ver $version" pentaho.spec
