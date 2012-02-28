%define _prefix /opt/pentaho-biserver
%define _prefix_admin /opt/pentaho-biserver-admin
%define CATALINA_HOME /usr/share/tomcat6

Name:		pentaho-biserver-tomcat
Version:	%{ver}
Release:	2%{?dist}
Summary:	Pentaho BI server
License:	GPL
URL:		http://www.pentaho.com
Source:		http://downloads.sourceforge.net/project/pentaho/BusinessIntelligenceServer/%{version}-stable/biserver-ce-%{version}-stable.tar.gz
Source1:	pentaho.init
Source2:	pentaho.pid
Source3:	postgresql-9.0-802.jdbc3.jar
Source4:	ojdbc14.jar
Source5:	orai18n.jar
Source6:        sqlitejdbc-v037-nested.jar
Source7:        mysql-connector-java-3.1.14-bin.jar
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:	/usr/sbin/groupadd /usr/sbin/useradd
Requires: 	java >= 1:1.6.0
Requires: 	tomcat6
Conflicts:      pentaho-biserver
BuildArch:	noarch

%description
%{summary}

%package        jdbc-drivers-tomcat
Summary:        jdbc drivers for pentaho
Group:          Applications/Database
Requires:       %{name}
%description    jdbc-drivers-tomcat
%{summary}

%prep
%setup -q -n biserver-ce


%build

%install
rm -rf $RPM_BUILD_ROOT
%__install -d "%{buildroot}%{_prefix}"
%__install -d "%{buildroot}%{CATALINA_HOME}"
%__install -d "%{buildroot}%{CATALINA_HOME}/lib"
%__install -d "%{buildroot}%{CATALINA_HOME}/webapps"

cp -pr "tomcat/webapps/pentaho" "%{buildroot}%{CATALINA_HOME}/webapps"
cp -pr "tomcat/webapps/pentaho-style" "%{buildroot}%{CATALINA_HOME}/webapps"
cp -pr "tomcat/webapps/sw-style" "%{buildroot}%{CATALINA_HOME}/webapps"
%__install -D -m0644 "%{SOURCE3}" "%{buildroot}%{CATALINA_HOME}/lib"
%__install -D -m0644 "%{SOURCE4}" "%{buildroot}%{CATALINA_HOME}/lib"
%__install -D -m0644 "%{SOURCE5}" "%{buildroot}%{CATALINA_HOME}/lib"
%__install -D -m0644 "%{SOURCE6}" "%{buildroot}%{CATALINA_HOME}/lib"
%__install -D -m0644 "%{SOURCE7}" "%{buildroot}%{CATALINA_HOME}/lib"

cp -pr pentaho-solutions "%{buildroot}%{_prefix}"
cp -pr data "%{buildroot}%{_prefix}"
cp -pr ../administration-console "%{buildroot}%{_prefix_admin}"

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,tomcat,tomcat,-)
%attr(0755,tomcat,tomcat) %dir %{_prefix}
%doc
%{_prefix}/pentaho-solutions
%{_prefix}/data
%{CATALINA_HOME}/webapps/pentaho
%{CATALINA_HOME}/webapps/pentaho-style
%{CATALINA_HOME}/webapps/sw-style
%{_prefix_admin}

%files jdbc-drivers-tomcat
%defattr(-,tomcat,tomcat,-)
%{CATALINA_HOME}/lib/postgresql-9.0-802.jdbc3.jar
%{CATALINA_HOME}/lib/mysql-connector-java-3.1.14-bin.jar
%{CATALINA_HOME}/lib/ojdbc14.jar
%{CATALINA_HOME}/lib/orai18n.jar
%{CATALINA_HOME}/lib/sqlitejdbc-v037-nested.jar
%{CATALINA_HOME}/lib/postgresql-9.0-802.jdbc3.jar

%pre
/usr/sbin/useradd -g tomcat -s /bin/false -r -c "tomcat server" \
-d "/usr/share/tomcat6" tomcat &>/dev/null || :

%post

%preun
if [ "$1" = 0 ] ; then
    # if this is uninstallation as opposed to upgrade, delete the service
    /sbin/service tomcat6 stop > /dev/null 2>&1
fi
exit 0

%postun
if [ "$1" -ge 1 ]; then
    /sbin/service tomcat6 condrestart > /dev/null 2>&1
fi
exit 0

%changelog
* Tue Feb 28 2012 Jean-Francois Roche <jfroche@affinitic.be>
- Add pentaho on an existing tomcat install

* Tue Dec 23 2011 Jean-Francois Roche <jfroche@affinitic.be>
- Add administration console server

* Tue Dec 20 2011 Jean-Francois Roche <jfroche@affinitic.be>
- Initial implementation

