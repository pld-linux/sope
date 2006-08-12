# TODO: descs for subpackages
#	Mysql and Sqlite backends
# - cleanup
# - bconds on DB backends
# - R and BRs
%define		trunkdate	200601231100
%define		sope_makeflags	-w -s debug=yes strip=no
%define		versionalpha	r1203

Summary:	SKYRiX Object Publishing Environment
Summary(pl):	SKYRiX Object Publishing Environment - ¶rodowisko do publikowania obiektów
Name:		sope
Version:	4.5
Release:	0.4
Vendor:		http://www.opengroupware.org/
License:	GPL
Group:		Libraries
Source0:	http://download.opengroupware.org/nightly/sources/trunk/%{name}-trunk-%{versionalpha}-%{trunkdate}.tar.gz
# Source0-md5:	c7b249efd88686d695f7815f8036db76
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

%define		prefix		%{_libdir}/GNUstep-libFoundation

%define		libcombo	gnu-fd-nil
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
formatu iCalendar. Poszczególne szkielety z tego pakietu mog± byæ
u¿ywane samodzielnie (na przyk³ad w aplikacjach Cocoa) i nie wymagaj±
samego serwera aplikacji.

%package xml
Summary:	SOPE libraries for XML processing
Summary(pl):	Biblioteki SOPE do przetwarzania XML
Group:		Libraries

%description xml
The SOPE libraries for XML processing contain:

- a SAX2 Implementation for Objective-C
- an attempt to implement DOM on top of SaxObjC
- an XML-RPC implementation (without a transport layer)

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description xml -l pl
Biblioteki SOPE do przetwarzania XML zawieraj±:

- implementacjê SAX2 dla Objective C
- próbê implementacji DOM w oparciu o SaxObjC
- implementacjê XML-RPC (bez warstwy transportowej)

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package xml-devel
Summary:	Development files for the SOPE XML libraries
Summary(pl):	Pliki programistyczne dla bibliotek SOPE XML
Group:		Development/Libraries
Requires:	%{name}-xml = %{version}-%{release}
Requires:	libxml2-devel
#Requires:	ogo-gnustep_make

%description xml-devel
This package contains the development files of the SOPE XML libraries.

%description xml-devel -l pl
Ten pakiet zawiera pliki programistyczne dla bibliotek SOPE XML.

%package xml-tools
Summary:	Tools (domxml/saxxml/xmln)
Summary(pl):	Narzêdzia (domxml/saxxml/xmln)
Group:		Development/Tools
Requires:	%{name}-xml = %{version}-%{release}

%description xml-tools
This package contains some tools:

- saxxml - parse a file using SAX and print out the XML
- xmln   - convert a given file to PYX using a SAX handler
- domxml - parse a file into a DOM and print out the XML

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description xml-tools
Ten pakiet zawiera nastêpuj±ce narzêdzia:

- saxxml - przetwarzanie pliku przy u¿yciu SAX i wypisywanie XML-a
- xmln   - zamiana podanego pliku na PYX przy u¿yciu handlera SAX
- domxml - przetwarzanie pliku na DOM i wypisywanie XML-a

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package core
Summary:	Core libraries of the SOPE application server
Summary(pl):	Podstawowe biblioteki serwera aplikacji SOPE
Group:		Libraries
Requires:	%{name}-xml = %{version}-%{release}
# should be autodetected
#Requires:	libfoundation

%description core
The SOPE core libraries contain:

- various Foundation extensions
- a java.io like stream and socket library

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description core -l pl
Podstawowe biblioteki SOPE zawieraj±:

- ró¿ne rozszerzenia Foundation
- bibliotekê strumieni i gniazd podobn± do java.io

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package core-devel
Summary:	Development files for the SOPE core libraries
Summary(pl):	Pliki programistyczne dla podstawowych bibliotek SOPE
Group:		Development/Libraries
#Requires:	ogo-gnustep_make

%description core-devel
This package contains the header files for the SOPE core
libraries, which are part of the SOPE application server framework.

%description core-devel -l pl
Ten pakiet zawiera pliki nag³ówkowe dla podstawowych bibliotek SOPE,
bêd±cych czê¶ci± szkieletu serwera aplikacji SOPE.

%package mime
Summary:	SOPE libraries for MIME processing
Summary(pl):	Biblioteki SOPE do przetwarzania MIME
Group:		Libraries
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-xml = %{version}-%{release}
# should be autodetected
#Requires:	libfoundation

%description mime
The SOPE libraries for MIME processing contain:

- classes for processing MIME entities
- a full IMAP4 implementation
- prototypical POP3 and SMTP processor

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description mime -l pl
Biblioteki SOPE do przetwarzania MIME zawieraj±:

- klasy do przetwarzania jednostek MIME
- pe³n± implementacjê IMAP4
- prototypowy procesor POP3 i SMTP

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package mime-devel
Summary:	Development files for the SOPE MIME libraries
Summary(pl):	Pliki programistyczne dla bibliotek SOPE MIME
Group:		Development/Libraries
#Requires:	ogo-gnustep_make

%description mime-devel
This package contains the development files of the SOPE MIME
libraries.

%description mime-devel -l pl
Ten pakiet zawiera pliki programistyczne dla bibliotek SOPE MIME.

%package appserver
Summary:	SOPE application server libraries
Summary(pl):	Biblioteki serwera aplikacji SOPE
Group:		Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-xml = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-mime = %{version}-%{release}
Requires:	glibc >= 6:2.3.5-7.6
# should be autodetected
#Requires:	libfoundation

%description appserver
The SOPE application server libraries provide:

- template rendering engine, lots of dynamic elements
- HTTP client/server
- XML-RPC client
- WebDAV server framework
- session management
- scripting extensions for Foundation, JavaScript bridge
- DOM tree rendering library

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description appserver -l pl
Biblioteki serwera aplikacji SOPE udostêpniaj±:

- silnik renderuj±cy szablony i wiele elementów dynamicznych
- klienta/serwer HTTP
- klienta XML-RPC
- szkielet serwera WebDAV
- zarz±dzanie sesjami
- rozszerzenia skryptowe dla Foundation oraz pomost dla JavaScriptu
- bibliotekê renderuj±c± drzewa DOM

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package appserver-devel
Summary:	Development files for the SOPE application server libraries
Summary(pl):	Pliki programistyczne dla bibliotek serwera aplikacji SOPE
Group:		Development/Libraries
Requires:	%{name}-appserver = %{version}-%{release}
#Requires:	ogo-gnustep_make

%description appserver-devel
This package contains the development files for the SOPE application
server libraries.

%description appserver-devel -l pl
Ten pakiet zawiera pliki programistyczne dla bibliotek serwera
aplikacji SOPE.

%package appserver-tools
Summary:	Tools shipped with the SOPE application server
Summary(pl):	Narzêdzia dostarczane z serwerem aplikacji SOPE
Group:		Development/Toole
Requires:	%{name}-appserver = %{version}-%{release}

%description appserver-tools
This package contains some tools shipped with the SOPE application
server framework, which are mostly useful for development and
debugging of SOPE applications.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description appserver-tools -l pl
Ten pakiet zawiera narzêdzia dostarczane ze szkieletem serwera
aplikacji SOPE, przydatne g³ównie do rozwijania i ¶ledzenia aplikacji
SOPE.

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package ldap
Summary:	SOPE libraries for LDAP access
Summary(pl):	Biblioteki SOPE do dostêpu do LDAP
Group:		Libraries
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-xml = %{version}-%{release}
# should be autodetected
#Requires:	libfoundation

%description ldap
The SOPE libraries for LDAP access contain an Objective-C wrapper for
LDAP directory services.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description ldap -l pl
Biblioteki SOPE do dostêpu do LDAP zawieraj± wrapper Objective-C dla
us³ug katalogowych LDAP.

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package ldap-devel
Summary:	Development files for the SOPE LDAP libraries
Summary(pl):	Pliki programistyczne dla bibliotek SOPE LDAP
Group:		Development/Libraries
Requires:	%{name}-ldap = %{version}-%{release}
#Requires:	ogo-gnustep_make

%description ldap-devel
This package contains the development files of the SOPE LDAP
libraries.

%description ldap-devel -l pl
Ten pakiet zawiera pliki programistyczne dla bibliotek SOPE LDAP.

%package ldap-tools
Summary:	Tools (ldap2dsml/ldapchkpwd/ldapls)
Summary(pl):	Narzêdzia (ldap2dsml/ldapchkpwd/ldapls)
Group:		Development/Tools
Requires:	%{name}-ldap = %{version}-%{release}

%description ldap-tools
This package contains some tools:

- ldap2dsml  - return the output of an LDAP server as DSML
               (Directory Service Markup Language)
- ldapchkpwd - checks whether a login/password combo would be authenticated
- ldapls     - an 'ls' for LDAP directories

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description ldap-tools -l pl
Ten pakiet zawiera nastêpuj±ce narzêdzia:

- ldap2dsml  - zwracanie wyj¶cia serwera LDAP jako DSML
               (Directory Service Markup Language - jêzyk znakowania
               us³ug katalogowych)
- ldapchkpwd - sprawdzanie, czy po³±czenie login/has³o jest poprawnie
               uwierzytelniane
- ldapls     - 'ls' dla katalogów LDAP

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package ical
Summary:	SOPE libraries for iCal handling
Summary(pl):	Biblioteki SOPE do obs³ugi iCal
Group:		Libraries
Requires:	%{name}-xml = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
# should be autodetected
#Requires:	libfoundation

%description ical
The SOPE libraries for iCal handling contain classes for iCalendar and
vCard objects.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description ical -l pl
Biblioteki SOPE do obs³ugi iCal zawieraj± klasy dla obiektów iCalendar
i vCard.

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package ical-devel
Summary:	Development files for the SOPE iCal libraries
Summary(pl):	Pliki programistyczne dla bibliotek SOPE iCal
Group:		Development/Libraries
Requires:	%{name}-ical = %{version}-%{release}
#Requires:	ogo-gnustep_make

%description ical-devel
This package contains the development files of the SOPE iCal
libraries.

%description ical-devel -l pl
Ten pakiet zawiera pliki programistyczne dla bibliotek SOPE iCal.

%package gdl1
Summary:	GNUstep database libraries for SOPE
Summary(pl):	Biblioteki GNUstepa do baz danych dla SOPE
Group:		Libraries
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-xml = %{version}-%{release}
# should be autodetected
#Requires:	libfoundation

%description gdl1
This package contains a fork of the GNUstep database libraries used
by the SOPE application server (including GDLContentStore).

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by
ZOPE.

%description gdl1 -l pl
Ten pakiet zawiera odga³êzienie bibliotek GNUstepa do baz danych
u¿ywane przez serwer aplikacji SOPE (wraz z GDLContentStore).

SOPE to szkielet do tworzenia aplikacji i us³ug WWW. Nazwa "SOPE"
(SKYRiX Object Publishing Environment) jest zainspirowana ZOPE.

%package gdl1-postgresql
Summary:	PostgreSQL connector for SOPE's fork of the GNUstep database environment
Summary(pl):	Modu³ PostgreSQL dla odga³êzienia SOPE ¶rodowiska baz danych GNUstepa
Group:		Libraries
Requires:	%{name}-gdl1 = %{version}-%{release}
# local database?
Requires:	postgresql

%description gdl1-postgresql
This package contains the PostgreSQL connector for SOPE's fork of the
GNUstep database libraries.

%description gdl1-postgresql -l pl
Ten pakiet zawiera modu³ PostgreSQL dla odga³êzienia SOPE bibliotek do
baz danych GNUstepa.

%package gdl1-mysql
Summary:	MySQL connector for SOPE's fork of the GNUstep database environment
Summary(pl):	Modu³ MySQL dla odga³êzienia SOPE ¶rodowiska baz danych GNUstepa
Group:		Libraries
Requires:	%{name}-gdl1 = %{version}-%{release}

%description gdl1-mysql
This package contains the MySQL connector for SOPE's fork of the
GNUstep database libraries.

%description gdl1-mysql -l pl
Ten pakiet zawiera modu³ MySQL dla odga³êzienia SOPE bibliotek do baz
danych GNUstepa.

#%package gdl1-sqlite3
#Summary:	SQLite3 connector for SOPE's fork of the GNUstep database environment
#Summary(pl):	Modu³ SQLite3 dla odga³êzienia SOPE ¶rodowiska baz danych GNUstepa
#Group:		Libraries
#Requires:	%{name}-gdl1 = %{version}-%{release}
#
#%description gdl1-sqlite3
#This package contains the SQLite3 connector for SOPE's fork of the
#GNUstep database libraries.
#
#%description gdl1-sqlite3 -l pl
#Ten pakiet zawiera modu³ SQLite3 dla odga³êzienia SOPE bibliotek do baz
#danych GNUstepa.

%package gdl1-tools
Summary:	Tools (gcs_cat/gcs_gensql/gcs_ls/gcs_mkdir/gcs_recreatequick)
Summary(pl):	Narzêdzia (gcs_cat/gcs_gensql/gcs_ls/gcs_mkdir/gcs_recreatequick)
Group:		Development/Tools
Requires:	%{name}-gdl1 = %{version}-%{release}

%description gdl1-tools
Various tools around the GDLContentStore.

%description gdl1-tools -l pl
Ró¿ne narzêdzia dla GDLContentStore.

%package gdl1-devel
Summary:	Development files for the GNUstep database libraries
Summary(pl):	Pliki programistyczne dla bibliotek do baz danych GNUstepa
Group:		Development/Libraries
Requires:	%{name}-gdl1 = %{version}-%{release}
#Requires:	ogo-gnustep_make
Requires:	postgresql-devel

%description gdl1-devel
This package contains the header files for SOPE's fork of the GNUstep
database libraries (including GDLContentStore).

%description gdl1-devel -l pl
Ten pakiet zawiera pliki nag³ówkowe dla odga³êzienia SOPE bibliotek do
baz danych GNUstepa (w³±cznie z GDLContentStore).

%prep
%setup -q -n %{name}

%build
. %{prefix}/System/Library/Makefiles/GNUstep.sh
export LIBRARY_COMBO=%{libcombo}
export LDFLAGS="-llibobjc.so.lf2 %{rpmldflags}"
./configure \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--gsmake=%{prefix}/System

%{__make} \
	all \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{prefix}/System \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo '%{prefix}/lib' > $RPM_BUILD_ROOT/etc/ld.so.conf.d/%{name}-appserver.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post	appserver -p /sbin/ldconfig
%postun	appserver -p /sbin/ldconfig

%post	xml -p /sbin/ldconfig
%postun	xml -p /sbin/ldconfig

%post	core -p /sbin/ldconfig
%postun	core -p /sbin/ldconfig

%post	mime -p /sbin/ldconfig
%postun	mime -p /sbin/ldconfig

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
%dir %{_libdir}/%{name}-%{version}/saxdrivers
%{_libdir}/%{name}-%{version}/saxdrivers/libxmlSAXDriver.sax
%{_libdir}/%{name}-%{version}/saxdrivers/STXSaxDriver.sax

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
/etc/ld.so.conf.d/%{name}-appserver.conf
%attr(755,root,root) %{_libdir}/libNGObjWeb*.so.%{version}*
%attr(755,root,root) %{_libdir}/libNGXmlRpc*.so.%{version}*
%attr(755,root,root) %{_libdir}/libSoOFS*.so.%{version}*
%attr(755,root,root) %{_libdir}/libWEExtensions*.so.%{version}*
%attr(755,root,root) %{_libdir}/libWOExtensions*.so.%{version}*
%attr(755,root,root) %{_libdir}/libWOXML*.so.%{version}*
%dir %{_datadir}/%{name}-%{version}/ngobjweb
%{_datadir}/%{name}-%{version}/ngobjweb/DAVPropMap.plist
%{_datadir}/%{name}-%{version}/ngobjweb/Defaults.plist
%{_datadir}/%{name}-%{version}/ngobjweb/Languages.plist
%dir %{_libdir}/%{name}-%{version}/products
%{_libdir}/%{name}-%{version}/products/SoCore.sxp
%{_libdir}/%{name}-%{version}/products/SoOFS.sxp
%dir %{_libdir}/%{name}-%{version}/wox-builders
%{_libdir}/%{name}-%{version}/wox-builders/WEExtensions.wox
%{_libdir}/%{name}-%{version}/wox-builders/WOExtensions.wox

%files appserver-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}-%{version}
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
%{prefix}/System/Library/Makefiles/Additional/ngobjweb.make
%{prefix}/System/Library/Makefiles/woapp.make
%{prefix}/System/Library/Makefiles/wobundle.make

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
%{_datadir}/%{name}-%{version}/saxmappings/NGiCal.xmap
%{_libdir}/%{name}-%{version}/saxdrivers/versitSaxDriver.sax

%files ical-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libNGiCal*.so
%{_includedir}/NGiCal

%files gdl1
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/connect-EOAdaptor
%attr(755,root,root) %{_bindir}/load-EOAdaptor
%attr(755,root,root) %{_libdir}/libGDLAccess*.so.%{version}*
%attr(755,root,root) %{_libdir}/libGDLContentStore*.so.%{version}*

%files gdl1-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/dbadaptors/PostgreSQL.gdladaptor

#%files gdl1-mysql
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/%{name}-%{version}/dbadaptors/MySQL.gdladaptor

#%files gdl1-sqlite3
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/%{name}-%{version}/dbadaptors/SQLite3.gdladaptor

%files gdl1-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gcs_cat
%attr(755,root,root) %{_bindir}/gcs_gensql
%attr(755,root,root) %{_bindir}/gcs_ls
%attr(755,root,root) %{_bindir}/gcs_mkdir
%attr(755,root,root) %{_bindir}/gcs_recreatequick

%files gdl1-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGDLAccess*.so
%attr(755,root,root) %{_libdir}/libGDLContentStore*.so
%{_includedir}/GDLAccess
%{_includedir}/GDLContentStore
