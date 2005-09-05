# TODO: descs for subpackages
#	Mysql and Sqlite backends
%define		trunkdate	200508311700
%define		sope_makeflags	-w -s debug=yes strip=no
%define		versionalpha	r1098

Summary:	SKYRiX Object Publishing Environment
Summary(pl):	SKYRiX Object Publishing Environment - ¶rodowisko do publikowania obiektów
Name:		sope
Version:	4.5
Release:	0.1
Vendor:		http://www.opengroupware.org/
License:	GPL
Group:		Development/Libraries
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-%{versionalpha}-%{trunkdate}.tar.gz
# Source0-md5:	22bf6213e39fdc8bdeaede293e419cfd
URL:		http://www.opengroupware.org/
BuildRequires:	STLport-devel >= 4.6.2
BuildRequires:	apache-devel >= 2.0.50
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils >= 2.15.90
BuildRequires:	bison
BuildRequires:	cyrus-sasl-devel >= 2.1.18
BuildRequires:	expat-devel >= 1.95.7
BuildRequires:	flex
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	glibc-devel >= 6:2.3.4
BuildRequires:	gnustep-base-devel >= 1.10.0
BuildRequires:	libffi-devel >= 3.3.5
#BuildRequires:	libfoundation-devel
BuildRequires:	libical
#BuildRequires:	libobjc-lf2-devel
BuildRequires:	libstdc++-devel >= 3.3.45
BuildRequires:	libtool >= 1.5.10
BuildRequires:	libxml >= 1.8.17
BuildRequires:	openldap-devel >= 2.2.17
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	postgresql-devel >= 7.4.0
#Requires:	apache >= 2.0.50
#Requires:	libfoundation
Requires:	libical-sope
Requires:	libobjc
#Requires:	libobjc-lf2
Requires:	libxml2 >= 2.6.14
Requires:	openldap >= 2.2.10
# does it really require local database?
#Requires:	postgresql >= 7.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif


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

%description xml
sope-xml

%package xml-devel
Summary:	sope-xml devel
Group:		Development/Libraries

%description xml-devel
sope-xml devel package.

%package xml-tools
Summary:	sope-xml tools
Group:		Development/Tools

%description xml-tools
sope-xml tools package.

%package core
Summary:	sope-core
Group:		Libraries

%description core
sope-core

%package core-devel
Summary:	sope-core devel
Group:		Development/Libraries

%description core-devel
sope-core devel package.

%package mime
Summary:	sope-mime
Group:		Libraries

%description mime
sope-mime

%package mime-devel
Summary:	sope-mime devel
Group:		Development/Libraries

%description mime-devel
sope-mime devel package.

%package appserver
Summary:	sope-appserver
Group:		Libraries

%description appserver
sope-appserver

%package appserver-devel
Summary:	sope-appserver devel
Group:		Development/Libraries

%description appserver-devel
sope-appserver devel package.

%package appserver-tools
Summary:	sope-appserver tools
Group:		Development/Tools

%description appserver-tools
sope-appserver tools package.

%package ldap
Summary:	sope-ldap
Group:		Libraries

%description ldap
sope-ldap

%package ldap-devel
Summary:	sope-ldap devel
Group:		Development/Libraries

%description ldap-devel
sope-ldap devel package.

%package ldap-tools
Summary:	sope-ldap tools
Group:		Development/Tools

%description ldap-tools
sope-ldap tools package.

%package ical
Summary:	sope-ical
Group:		Libraries

%description ical
sope-ical

%package ical-devel
Summary:	sope-ical devel
Group:		Development/Libraries

%description ical-devel
sope-ical devel package.

%package gdl1
Summary:	sope-gdl1
Group:		Libraries

%description gdl1
sope-gdl1

%package gdl1-postgresql
Summary:	sope-gdl1-postgresql
Group:		Libraries

%description gdl1-postgresql
sope-gdl1-postgresql

%package gdl1-devel
Summary:	sope-gdl1 devel
Group:		Development/Libraries

%description gdl1-devel
sope-gdl1 devel package.

%package EOF
Summary:	Enterprise Objects Framework
Summary(pl):	Szkielet Enterprise Objects Framework
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description EOF
Enterprise Objects Framework.

%description EOF -l pl
Szkielet Enterprise Objects Framework.

%package EOF-devel
Summary:	Headers for Enterprise Objects Framework
Summary(pl):	Pliki nag³ówkowe dla szkieletu Enterprise Objects Framework
Group:		Development/Libraries
Requires:	%{name}-EOF = %{version}-%{release}

%description EOF-devel
Headers for Enterprise Objects Framework.

%description EOF-devel -l pl
Pliki nag³ówkowe dla szkieletu Enterprise Objects Framework.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
./configure --with-gnustep
%{__make} \
	all \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT

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

%post	EOF -p /sbin/ldconfig
%postun	EOF -p /sbin/ldconfig


%files xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libDOM*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libSaxObjC*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libXmlRpc*.so.%{version}*
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax/%{gscpu}
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax/%{gscpu}/%{gsos}/%{libcombo}
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax/%{gscpu}
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax/%{gscpu}/%{gsos}/%{libcombo}
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax/Resources
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax/Resources
%attr(755,root,root) %{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax/%{gscpu}/%{gsos}/%{libcombo}/*
%attr(755,root,root) %{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax/%{gscpu}/%{gsos}/%{libcombo}/*
%{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax/*.plist
%{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax/Resources/*.plist
%{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax/Resources/*.plist
%{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax/*.plist
%{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax/Resources/Version
%{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax/Resources/Version
%{_prefix}/System/Library/SaxDrivers-%{version}/libxmlSAXDriver.sax/stamp.make
%{_prefix}/System/Library/SaxDrivers-%{version}/STXSaxDriver.sax/stamp.make

%files xml-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/domxml
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/saxxml
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/xmln

%files xml-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libDOM*.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libSaxObjC*.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libXmlRpc*.so
%{_prefix}/System/Library/Headers/%{libcombo}/DOM
%{_prefix}/System/Library/Headers/%{libcombo}/SaxObjC
%{_prefix}/System/Library/Headers/%{libcombo}/XmlRpc

%files core
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGExtensions*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGStreams*.so.%{version}*

%files core-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGExtensions*.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGStreams*.so
%{_prefix}/System/Library/Headers/%{libcombo}/NGExtensions
%{_prefix}/System/Library/Headers/%{libcombo}/NGStreams

%files mime
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGMime*.so.%{version}*

%files mime-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGMime*.so
%{_prefix}/System/Library/Headers/%{libcombo}/NGImap4
%{_prefix}/System/Library/Headers/%{libcombo}/NGMail
%{_prefix}/System/Library/Headers/%{libcombo}/NGMime

%files appserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGObjWeb*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGXmlRpc*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libSoOFS*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libWEExtensions*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libWOExtensions*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libWOXML*.so.%{version}*
%dir %{_prefix}/System/Library/SaxDrivers-%{version}
%dir %{_prefix}/System/Library/Libraries/Resources/NGObjWeb
%{_prefix}/System/Library/Libraries/Resources/NGObjWeb/*.plist
%dir %{_prefix}/System/Library/SoProducts-%{version}
%dir %{_prefix}/System/Library/SoProducts-%{version}/*.sxp
%dir %{_prefix}/System/Library/SoProducts-%{version}/*.sxp/Resources
%{_prefix}/System/Library/SoProducts-%{version}/*.sxp/Resources/*.plist
%{_prefix}/System/Library/SoProducts-%{version}/*.sxp/Resources/Version
%dir %{_prefix}/System/Library/SoProducts-%{version}/*.sxp/%{gscpu}
%dir %{_prefix}/System/Library/SoProducts-%{version}/*.sxp/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/SoProducts-%{version}/*.sxp/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Library/SoProducts-%{version}/*.sxp/%{gscpu}/%{gsos}/%{libcombo}/*
%{_prefix}/System/Library/SoProducts-%{version}/*.sxp/stamp.make
%dir %{_prefix}/System/Library/WOxElemBuilders-%{version}
%dir %{_prefix}/System/Library/WOxElemBuilders-%{version}/*.wox
%{_prefix}/System/Library/WOxElemBuilders-%{version}/*.wox/*.plist
%dir %{_prefix}/System/Library/WOxElemBuilders-%{version}/*.wox/Resources
%{_prefix}/System/Library/WOxElemBuilders-%{version}/*.wox/Resources/*.plist
%{_prefix}/System/Library/WOxElemBuilders-%{version}/*.wox/stamp.make
%dir %{_prefix}/System/Library/WOxElemBuilders-%{version}/*.wox/%{gscpu}
%dir %{_prefix}/System/Library/WOxElemBuilders-%{version}/*.wox/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/WOxElemBuilders-%{version}/*.wox/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Library/WOxElemBuilders-%{version}/*.wox/%{gscpu}/%{gsos}/%{libcombo}/*

%files appserver-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/gcs_*
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/rss*
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/sope-%{version}
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/testqp
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/xmlrpc_call

%files appserver-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/wod
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGObjWeb*.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGXmlRpc*.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libSoOFS*.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libWEExtensions*.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libWOExtensions*.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libWOXML*.so
%{_prefix}/System/Library/Headers/%{libcombo}/NGHttp
%{_prefix}/System/Library/Headers/%{libcombo}/NGObjWeb
%{_prefix}/System/Library/Headers/%{libcombo}/NGXmlRpc
%{_prefix}/System/Library/Headers/%{libcombo}/SoOFS
%{_prefix}/System/Library/Headers/%{libcombo}/WEExtensions
%{_prefix}/System/Library/Headers/%{libcombo}/WOExtensions
%{_prefix}/System/Library/Headers/%{libcombo}/WOXML
%{_prefix}/System/Library/Makefiles/Additional/ngobjweb.make
%{_prefix}/System/Library/Makefiles/woapp.make
%{_prefix}/System/Library/Makefiles/wobundle.make

%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGLdap*.so.%{version}*

%files ldap-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/ldap2dsml
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/ldapchkpwd
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/ldapls

%files ldap-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGLdap*.so
%{_prefix}/System/Library/Headers/%{libcombo}/NGLdap

%files ical
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGiCal*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/SaxDrivers-%{version}/versitSaxDriver.sax/%{gscpu}/%{gsos}/%{libcombo}/*
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/versitSaxDriver.sax
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/versitSaxDriver.sax/Resources
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/versitSaxDriver.sax/%{gscpu}
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/versitSaxDriver.sax/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/SaxDrivers-%{version}/versitSaxDriver.sax/%{gscpu}/%{gsos}/%{libcombo}
%dir %{_prefix}/System/Library/SaxMappings
%{_prefix}/System/Library/SaxDrivers-%{version}/versitSaxDriver.sax/*.plist
%{_prefix}/System/Library/SaxDrivers-%{version}/versitSaxDriver.sax/Resources/*.plist
%{_prefix}/System/Library/SaxMappings/NGiCal.xmap
%{_prefix}/System/Library/SaxDrivers-%{version}/versitSaxDriver.sax/stamp.make


%files ical-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGiCal*.so
%{_prefix}/System/Library/Headers/%{libcombo}/NGiCal

%files gdl1
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/connect-EOAdaptor
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/load-EOAdaptor
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libGDLAccess*.so.%{version}*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libGDLContentStore*.so.%{version}*

%files gdl1-postgresql
%defattr(644,root,root,755)
%dir %{_prefix}/System/Library/GDLAdaptors-%{version}
%dir %{_prefix}/System/Library/GDLAdaptors-%{version}/*.gdladaptor
%{_prefix}/System/Library/GDLAdaptors-%{version}/*.gdladaptor/stamp.make
%dir %{_prefix}/System/Library/GDLAdaptors-%{version}/*.gdladaptor/Resources
%{_prefix}/System/Library/GDLAdaptors-%{version}/*.gdladaptor/Resources/*
%dir %{_prefix}/System/Library/GDLAdaptors-%{version}/*.gdladaptor/%{gscpu}
%dir %{_prefix}/System/Library/GDLAdaptors-%{version}/*.gdladaptor/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/GDLAdaptors-%{version}/*.gdladaptor/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Library/GDLAdaptors-%{version}/*.gdladaptor/%{gscpu}/%{gsos}/%{libcombo}/*

%files gdl1-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libGDLAccess*.so
%{_prefix}/System/Library/Headers/%{libcombo}/GDLAccess
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libGDLContentStore*.so
%{_prefix}/System/Library/Headers/%{libcombo}/GDLContentStore

%files EOF
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libEOControl*.so.%{version}*

%files EOF-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libEOControl*.so
%{_prefix}/System/Library/Headers/%{libcombo}/EOControl
