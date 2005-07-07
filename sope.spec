# TODO: descs for subpackages
%define		trunkdate	200507061800
%define		sope_makeflags	-w -s debug=yes strip=no
%define		versionalpha	r868

Summary:	SKYRiX Object Publishing Environment
Summary(pl):	SKYRiX Object Publishing Environment - ¶rodowisko do publikowania obiektów
Name:		sope
Version:	4.5
Release:	0.1
Vendor:		http://www.opengroupware.org/
License:	GPL
Group:		Development/Libraries
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-%{versionalpha}-%{trunkdate}.tar.gz
# Source0-md5:	c22e4626419619e7c76c9c7640fce7ca
URL:		http://www.opengroupware.org/
#AutoReqProv:	off
BuildRequires:	STLport-devel >= 4.6.2
BuildRequires:	apache-devel >= 2.0.50
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils >= 2.15.90
BuildRequires:	bison
BuildRequires:	cyrus-sasl-devel >= 2.1.18
BuildRequires:	expat-devel >= 1.95.7
BuildRequires:	ffcall-devel >= 1.10
BuildRequires:	flex
BuildRequires:	gcc-objc
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	glibc-devel >= 6:2.3.4
BuildRequires:	gmp-devel >= 4.1.2
BuildRequires:	gnustep-base-devel >= 1.10.0
BuildRequires:	gnustep-make >= 1.10.0
BuildRequires:	gnustep-make-devel >= 1.10.0
BuildRequires:	libffi-devel >= 3.3.5
BuildRequires:	libfoundation-devel
BuildRequires:	libical
BuildRequires:	libobjc-lf2-devel
BuildRequires:	libstdc++-devel >= 3.3.45
BuildRequires:	libtool >= 1.5.10
BuildRequires:	libxml >= 1.8.17
BuildRequires:	libxml2-devel >= 2.6.14
BuildRequires:	openldap-devel >= 2.2.17
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	postgresql-devel >= 7.4.0
BuildRequires:	zlib-devel >= 1.2.1
Requires:	apache >= 2.0.50
Requires:	libfoundation
Requires:	libical-sope
#Requires:	libobjc
Requires:	libobjc-lf2
Requires:	libxml2 >= 2.6.14
Requires:	openldap >= 2.2.10
# does it really require local database?
Requires:	postgresql >= 7.2.0
Requires:	zlib >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SOPE package is an extensive set of frameworks (16 frameworks,
~1500 classes) which form a complete Web application server
environment. Besides the Apple WebObjects compatible appserver
extended with Zope concepts, it contains a large set of reusable
classes: XML processing (SAX2, DOM, XML-RPC), MIME/IMAP4 processing,
LDAP connectivity, RDBMS connectivity, and iCalendar parsing.
The individual frameworks of the package can be used standalone (for
example in Cocoa applications) and do not require the application
server itself.

%description -l pl
Pakiet SOPE to obszerny zestaw szkieletów (16 szkieletów, ~1500 klas)
tworz±cych kompletne ¶rodowisko serwera aplikacji WWW. Oprócz serwera
aplikacji zgodnego z Apple WebObjects rozszerzonego przez idee Zope
zawiera du¿y zbiór klas wielokrotnego u¿ycia do: przetwarzania XML
(SAX2, DOM, XML-RPC), przetwarzania MIME/IMAP4, ³±czno¶ci z LDAP,
³±czno¶ci z serwerami relacyjnych baz danych oraz przetwarzania
formatu iCalendar.

%package xml
Summary:	sope-xml
Group:		Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description xml
sope-xml

%package xml-devel
Summary:	sope-xml devel
Group:		Development/Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description xml-devel
sope-xml devel package.

%package xml-tools
Summary:	sope-xml tools
Group:		Development/Tools
#Requires:	gnustep-make
#AutoReqProv:	off

%description xml-tools
sope-xml tools package.

%package core
Summary:	sope-core
Group:		Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description core
sope-core

%package core-devel
Summary:	sope-core devel
Group:		Development/Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description core-devel
sope-core devel package.

%package mime
Summary:	sope-mime
Group:		Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description mime
sope-mime

%package mime-devel
Summary:	sope-mime devel
Group:		Development/Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description mime-devel
sope-mime devel package.

%package appserver
Summary:	sope-appserver
Group:		Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description appserver
sope-appserver

%package appserver-devel
Summary:	sope-appserver devel
Group:		Development/Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description appserver-devel
sope-appserver devel package.

%package appserver-tools
Summary:	sope-appserver tools
Group:		Development/Tools
#Requires:	gnustep-make
#AutoReqProv:	off

%description appserver-tools
sope-appserver tools package.

%package ldap
Summary:	sope-ldap
Group:		Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description ldap
sope-ldap

%package ldap-devel
Summary:	sope-ldap devel
Group:		Development/Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description ldap-devel
sope-ldap devel package.

%package ldap-tools
Summary:	sope-ldap tools
Group:		Development/Tools
#Requires:	gnustep-make
#AutoReqProv:	off

%description ldap-tools
sope-ldap tools package.

%package ical
Summary:	sope-ical
Group:		Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description ical
sope-ical

%package ical-devel
Summary:	sope-ical devel
Group:		Development/Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description ical-devel
sope-ical devel package.

%package gdl1
Summary:	sope-gdl1
Group:		Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description gdl1
sope-gdl1

%package gdl1-postgresql
Summary:	sope-gdl1-postgresql
Group:		Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description gdl1-postgresql
sope-gdl1-postgresql

%package gdl1-devel
Summary:	sope-gdl1 devel
Group:		Development/Libraries
#Requires:	gnustep-make
#AutoReqProv:	off

%description gdl1-devel
sope-gdl1 devel package.

%prep
%setup -q -n sope

%build
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%{__make} %{sope_makeflags} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
install -d $RPM_BUILD_ROOT%{_libdir}
%{__make} %{sope_makeflags} install \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix} \
	FHS_INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix}

rm -f $RPM_BUILD_ROOT%{_bindir}/rss2plist1
rm -f $RPM_BUILD_ROOT%{_bindir}/rss2plist2
rm -f $RPM_BUILD_ROOT%{_bindir}/rssparse
rm -f $RPM_BUILD_ROOT%{_bindir}/testqp

%clean
rm -rf $RPM_BUILD_ROOT

%post	xml -p /sbin/ldconfig
%postun	xml -p /sbin/ldconfig

%post	core -p /sbin/ldconfig
%postun	core -p /sbin/ldconfig

%post	mime -p /sbin/ldconfig
%postun	mime -p /sbin/ldconfig

%post	appserver -p /sbin/ldconfig
%postun	appserver -p /sbin/ldconfig

%post	ldap -p /sbin/ldconfig
%postun	ldap -p /sbin/ldconfig

%post	ical -p /sbin/ldconfig
%postun	ical -p /sbin/ldconfig

%post	gdl1 -p /sbin/ldconfig
%postun	gdl1 -p /sbin/ldconfig

%files xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libDOM*.so.%{version}*
%attr(755,root,root) %{_libdir}/libSaxObjC*.so.%{version}*
%attr(755,root,root) %{_libdir}/libXmlRpc*.so.%{version}*
# XXX: missing %{_libdir}/sope-%{version} dir
%dir %{_libdir}/sope-%{version}/saxdrivers
%{_libdir}/sope-%{version}/saxdrivers/libxmlSAXDriver.sax
%{_libdir}/sope-%{version}/saxdrivers/STXSaxDriver.sax

%files xml-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/domxml
%attr(755,root,root) %{_bindir}/saxxml
%attr(755,root,root) %{_bindir}/xmln

%files xml-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libDOM*.so
%attr(755,root,root) %{_libdir}/libSaxObjC*.so
%attr(755,root,root) %{_libdir}/libXmlRpc*.so
%{_includedir}/DOM
%{_includedir}/SaxObjC
%{_includedir}/XmlRpc

%files core
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libEOControl*.so.%{version}*
%attr(755,root,root) %{_libdir}/libNGExtensions*.so.%{version}*
%attr(755,root,root) %{_libdir}/libNGStreams*.so.%{version}*

%files core-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libEOControl*.so
%attr(755,root,root) %{_libdir}/libNGExtensions*.so
%attr(755,root,root) %{_libdir}/libNGStreams*.so
%{_includedir}/EOControl
%{_includedir}/NGExtensions
%{_includedir}/NGStreams

%files mime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libNGMime*.so.%{version}*

%files mime-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libNGMime*.so
%{_includedir}/NGImap4
%{_includedir}/NGMail
%{_includedir}/NGMime

%files appserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libNGObjWeb*.so.%{version}*
%attr(755,root,root) %{_libdir}/libNGXmlRpc*.so.%{version}*
%attr(755,root,root) %{_libdir}/libSoOFS*.so.%{version}*
%attr(755,root,root) %{_libdir}/libWEExtensions*.so.%{version}*
%attr(755,root,root) %{_libdir}/libWOExtensions*.so.%{version}*
%attr(755,root,root) %{_libdir}/libWOXML*.so.%{version}*
# XXX: missing {%{_datadir},%{_libdir}}/sope-%{version} dirs
%dir %{_datadir}/sope-%{version}/ngobjweb
%{_datadir}/sope-%{version}/ngobjweb/DAVPropMap.plist
%{_datadir}/sope-%{version}/ngobjweb/Defaults.plist
%{_datadir}/sope-%{version}/ngobjweb/Languages.plist
%dir %{_libdir}/sope-%{version}/products
%{_libdir}/sope-%{version}/products/SoCore.sxp
%{_libdir}/sope-%{version}/products/SoOFS.sxp
%dir %{_libdir}/sope-%{version}/wox-builders
%{_libdir}/sope-%{version}/wox-builders/WEExtensions.wox
%{_libdir}/sope-%{version}/wox-builders/WOExtensions.wox

%files appserver-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sope-%{version}
%attr(755,root,root) %{_bindir}/xmlrpc_call

%files appserver-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wod
%attr(755,root,root) %{_libdir}/libNGObjWeb*.so
%attr(755,root,root) %{_libdir}/libNGXmlRpc*.so
%attr(755,root,root) %{_libdir}/libSoOFS*.so
%attr(755,root,root) %{_libdir}/libWEExtensions*.so
%attr(755,root,root) %{_libdir}/libWOExtensions*.so
%attr(755,root,root) %{_libdir}/libWOXML*.so
%{_includedir}/NGHttp
%{_includedir}/NGObjWeb
%{_includedir}/NGXmlRpc
%{_includedir}/SoOFS
%{_includedir}/WEExtensions
%{_includedir}/WOExtensions
%{_includedir}/WOXML
%{_libdir}/GNUstep/System/Library/Makefiles/Additional/ngobjweb.make
%{_libdir}/GNUstep/System/Library/Makefiles/woapp.make
%{_libdir}/GNUstep/System/Library/Makefiles/wobundle.make

%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libNGLdap*.so.%{version}*

%files ldap-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ldap2dsml
%attr(755,root,root) %{_bindir}/ldapchkpwd
%attr(755,root,root) %{_bindir}/ldapls

%files ldap-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libNGLdap*.so
%{_includedir}/NGLdap

%files ical
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libNGiCal*.so.%{version}*
%{_datadir}/sope-%{version}/saxmappings/NGiCal.xmap
#%{_libdir}/sope-%{version}/saxdrivers/iCalSaxDriver.sax

%files ical-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libNGiCal*.so
%{_includedir}/NGiCal

%files gdl1
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/connect-EOAdaptor
%attr(755,root,root) %{_bindir}/load-EOAdaptor
%attr(755,root,root) %{_libdir}/libGDLAccess*.so.4.5*

%files gdl1-postgresql
%defattr(644,root,root,755)
%{_libdir}/sope-%{version}/dbadaptors/PostgreSQL.gdladaptor

%files gdl1-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGDLAccess*.so
%{_includedir}/GDLAccess
