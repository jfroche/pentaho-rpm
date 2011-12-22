%define _prefix /opt/pentaho-biserver

Name:		pentaho-biserver
Version:	%{ver}
Release:	1%{?dist}
Summary:	Pentaho BI server
License:	GPL
URL:		http://www.pentaho.com
Source:		http://downloads.sourceforge.net/project/pentaho/BusinessIntelligenceServer/%{version}-stable/biserver-ce-%{version}-stable.tar.gz
Source1:	pentaho.init
Source2:	pentaho.pid
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:	/usr/sbin/groupadd /usr/sbin/useradd
Requires: 	java >= 1:1.6.0
BuildArch:	noarch

%description


%prep
%setup -q -n biserver-ce


%build

%install
rm -rf $RPM_BUILD_ROOT
%__install -d "%{buildroot}%{_prefix}"
%__install -D -m0755 "%{SOURCE1}" "%{buildroot}/etc/init.d/pentaho"
%__install -D -m0600 "%{SOURCE2}" "%{buildroot}/var/run/pentaho.pid"
%__install -D -m0755 "start-pentaho.sh" "%{buildroot}%{_prefix}/start.sh"
%__install -D -m0755 "stop-pentaho.sh" "%{buildroot}%{_prefix}/stop.sh"
%__install -D -m0755 "set-pentaho-env.sh" "%{buildroot}%{_prefix}/set-pentaho-env.sh"

cp -pr tomcat "%{buildroot}%{_prefix}"
cp -pr pentaho-solutions "%{buildroot}%{_prefix}"
cp -pr data "%{buildroot}%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,pentaho,pentaho,-)
%attr(0755,pentaho,pentaho) %dir %{_prefix}
%doc
%dir %{_prefix}
%{_prefix}/start.sh
%{_prefix}/stop.sh
%{_prefix}/set-pentaho-env.sh
%{_prefix}/tomcat
%{_prefix}/pentaho-solutions
%{_prefix}/data
/etc/init.d/pentaho
/var/run/pentaho.pid
%exclude %{_prefix}/tomcat/bin/*.bat
%exclude %{_prefix}/tomcat/bin/*.exe
%exclude %{_prefix}/tomcat/bin/*.tar.gz
%exclude %{_prefix}/tomcat/bin/*.dll

%pre
/usr/sbin/groupadd -r pentaho &>/dev/null || :
/usr/sbin/useradd -g pentaho -s /bin/false -r -c "pentaho bi" \
-d "%{_prefix}" pentaho &>/dev/null || :

%post
/sbin/chkconfig --add pentaho

%preun
if [ "$1" = 0 ] ; then
    # if this is uninstallation as opposed to upgrade, delete the service
    /sbin/service pentaho stop > /dev/null 2>&1
    /sbin/chkconfig --del pentaho
fi
exit 0

%postun
if [ "$1" -ge 1 ]; then
    /sbin/service pentaho condrestart > /dev/null 2>&1
fi
exit 0

%changelog
* Tue Dec 20 2011 Jean-Francois Roche <jfroche@affinitic.be>
- Initial implementation

