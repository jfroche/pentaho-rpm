%define _prefix /opt/pentaho-pdi

Name:		pentaho-pdi
Version:	%{ver}
Release:	2%{?dist}
Summary:	Pentaho PDI
License:	GPL
URL:		http://www.pentaho.com
Source:		http://sourceforge.net/projects/pentaho/files/Data%20Integration/%{version}-stable/pdi-ce-%{version}-stable.tar.gz
Source1:	postgresql-9.0-802.jdbc4.jar
Source2:	ojdbc14.jar
Source3:	orai18n.jar
Source4:        sqlitejdbc-v037-nested.jar
Source5:        mysql-connector-java-3.1.14-bin.jar
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:	/usr/sbin/groupadd /usr/sbin/useradd
Requires: 	java >= 1:1.6.0
BuildArch:	x86_64

%description
%{summary}

%package        jdbc-drivers
Summary:        jdbc drivers for pentaho
Group:          Applications/Database
Requires:       %{name}
%description    jdbc-drivers
%{summary}

%prep
%setup -q -n data-integration


%build

%install
rm -rf $RPM_BUILD_ROOT
%__install -d "%{buildroot}%{_prefix}"

cp -pr launcher "%{buildroot}%{_prefix}"
cp -pr lib "%{buildroot}%{_prefix}"
cp -pr libext "%{buildroot}%{_prefix}"
cp -pr libswt "%{buildroot}%{_prefix}"
cp -pr plugins "%{buildroot}%{_prefix}"
cp -pr pwd "%{buildroot}%{_prefix}"
cp -pr simple-jndi "%{buildroot}%{_prefix}"

%__install -D -m0755 "carte.sh" "%{buildroot}%{_prefix}/carte.sh"
%__install -D -m0755 "encr.sh" "%{buildroot}%{_prefix}/encr.sh"
%__install -D -m0755 "generateClusterSchema.sh" "%{buildroot}%{_prefix}/generateClusterSchema.sh"
%__install -D -m0755 "kitchen.sh" "%{buildroot}%{_prefix}/kitchen.sh"
%__install -D -m0755 "pan.sh" "%{buildroot}%{_prefix}/pan.sh"

%__install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_prefix}/libext/JDBC"
%__install -D -m0644 "%{SOURCE2}" "%{buildroot}%{_prefix}/libext/JDBC"
%__install -D -m0644 "%{SOURCE3}" "%{buildroot}%{_prefix}/libext/JDBC"
%__install -D -m0644 "%{SOURCE4}" "%{buildroot}%{_prefix}/libext/JDBC"
%__install -D -m0644 "%{SOURCE5}" "%{buildroot}%{_prefix}/libext/JDBC"

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,pentaho,pentaho,-)
%attr(0755,pentaho,pentaho) %dir %{_prefix}
%doc
%{_prefix}/carte.sh
%{_prefix}/encr.sh
%{_prefix}/generateClusterSchema.sh
%{_prefix}/kitchen.sh
%{_prefix}/pan.sh

%{_prefix}/launcher
%{_prefix}/lib
%{_prefix}/libext
%{_prefix}/libswt
%{_prefix}/plugins
%{_prefix}/pwd
%{_prefix}/simple-jndi

%files jdbc-drivers
%defattr(-,pentaho,pentaho,-)
%{_prefix}/libext/JDBC/mysql-connector-java-3.1.14-bin.jar
%{_prefix}/libext/JDBC/ojdbc14.jar
%{_prefix}/libext/JDBC/orai18n.jar
%{_prefix}/libext/JDBC/sqlitejdbc-v037-nested.jar
%{_prefix}/libext/JDBC/postgresql-9.0-802.jdbc4.jar

%pre
/usr/sbin/groupadd -r pentaho &>/dev/null || :
/usr/sbin/useradd -g pentaho -s /bin/false -r -c "pentaho bi" \
-d "%{_prefix}" pentaho &>/dev/null || :

%changelog
* Tue Jan 18 2012 Jean-Francois Roche <jfroche@affinitic.be>
- Initial implementation
