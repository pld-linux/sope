# TODO: descs for subpackages
#	Mysql and Sqlite backends
# - cleanup
# - translations
# - bconds ond DB backends
# - R and BRs
%define		trunkdate	200509061700
%define		sope_makeflags	-w -s debug=yes strip=no
%define		versionalpha	r1101

Summary:	SKYRiX Object Publishing Environment
Summary(pl):	SKYRiX Object Publishing Environment - ¶rodowisko do publikowania obiektów
Name:		sope
Version:	4.5
Release:	0.3
Vendor:		http://www.opengroupware.org/
License:	GPL
Group:		Development/Libraries
Source0:	http://download.opengroupware.org/nightly/sources/trunk/%{name}-trunk-%{versionalpha}-%{trunkdate}.tar.gz
# Source0-md5:	2ee4dd3826cac5f8d44017af2462dfb3
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

%define         prefix         %{_libdir}/GNUstep-libFoundation

%define		libcombo	gnu-fd-nil
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%define 		sope_libversion		4.5
%define		sope_major_version	4
%define		sope_minor_version	5


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

#########################################
%package xml
Summary:      SOPE libraries for XML processing
Group:        Development/Libraries
AutoReqProv:  off

%description xml
The SOPE libraries for XML processing contain:

  * a SAX2 Implementation for Objective-C
  * an attempt to implement DOM on top of SaxObjC
  * an XML-RPC implementation (without a transport layer)

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package xml-devel
Summary:      Development files for the SOPE XML libraries
Group:        Development/Libraries
Requires:     ogo-gnustep_make sope%{sope_major_version}%{sope_minor_version}-xml libxml2-devel
AutoReqProv:  off

%description xml-devel
This package contains the development files of the SOPE XML libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package xml-tools
Summary:      Tools (domxml/saxxml/xmln)
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-xml
AutoReqProv:  off

%description xml-tools
This package contains some tools:

  * saxxml    - parse a file using SAX and print out the XML
  * xmln      - convert a given file to PYX using a SAX handler
  * domxml    - parse a file into a DOM and print out the XML

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.
#########################################
%package core
Summary:      Core libraries of the SOPE application server
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-xml libfoundation%{lfmaj}%{lfmin}
AutoReqProv:  off

%description core
The SOPE core libraries contain:

  * various Foundation extensions
  * a java.io like stream and socket library

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package core-devel
Summary:      Development files for the SOPE core libraries
Group:        Development/Libraries
Requires:     ogo-gnustep_make sope%{sope_major_version}%{sope_minor_version}-core
AutoReqProv:  off

%description core-devel
This package contains the header files for the SOPE core
libraries,  which are part of the SOPE application server framework.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.
#########################################
%package mime
Summary:      SOPE libraries for MIME processing
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-core sope%{sope_major_version}%{sope_minor_version}-xml libfoundation%{lfmaj}%{lfmin}
AutoReqProv:  off

%description mime
The SOPE libraries for MIME processing contain:

  * classes for processing MIME entities
  * a full IMAP4 implementation
  * prototypical POP3 and SMTP processor

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package mime-devel
Summary:      Development files for the SOPE MIME libraries
Group:        Development/Libraries
Requires:     ogo-gnustep_make sope%{sope_major_version}%{sope_minor_version}-mime
AutoReqProv:  off

%description mime-devel
This package contains the development files of the SOPE
MIME libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.
#########################################
%package appserver
Summary:      SOPE application server libraries
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-xml sope%{sope_major_version}%{sope_minor_version}-core sope%{sope_major_version}%{sope_minor_version}-mime libfoundation%{lfmaj}%{lfmin}
AutoReqProv:  off

%description appserver
The SOPE application server libraries provide:

  * template rendering engine, lots of dynamic elements
  * HTTP client/server
  * XML-RPC client
  * WebDAV server framework
  * session management
  * scripting extensions for Foundation, JavaScript bridge
  * DOM tree rendering library

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package appserver-devel
Summary:      Development files for the SOPE application server libraries
Group:        Development/Libraries
Requires:     ogo-gnustep_make sope%{sope_major_version}%{sope_minor_version}-appserver
AutoReqProv:  off

%description appserver-devel
This package contains the development files for the SOPE application server
libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package appserver-tools
Summary:      Tools shipped with the SOPE application server
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-appserver
AutoReqProv:  off

%description appserver-tools
This package contains some tools shipped with the SOPE application
server framework, which are mostly useful for development and debugging
of SOPE applications.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.
#########################################
%package ldap
Summary:      SOPE libraries for LDAP access
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-core sope%{sope_major_version}%{sope_minor_version}-xml libfoundation%{lfmaj}%{lfmin}
AutoReqProv:  off

%description ldap
The SOPE libraries for LDAP access contain an Objective-C wrapper for
LDAP directory services.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package ldap-devel
Summary:      Development files for the SOPE LDAP libraries
Group:        Development/Libraries
Requires:     ogo-gnustep_make sope%{sope_major_version}%{sope_minor_version}-ldap
AutoReqProv:  off

%description ldap-devel
This package contains the development files of the SOPE
LDAP libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package ldap-tools
Summary:      Tools (ldap2dsml/ldapchkpwd/ldapls)
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-ldap
AutoReqProv:  off

%description ldap-tools
This package contains some tools:

  * ldap2dsml   - return the output of an LDAP server as DSML
                  (directory service markup language)
  * ldapchkpwd  - checks whether a login/password combo would be authenticated
  * ldapls      - an 'ls' for LDAP directories

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.
#########################################
%package ical
Summary:      SOPE libraries for iCal handling
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-xml sope%{sope_major_version}%{sope_minor_version}-core libfoundation%{lfmaj}%{lfmin}
AutoReqProv:  off

%description ical
The SOPE libraries for iCal handling contain classes for iCalendar and
vCard objects.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package ical-devel
Summary:      Development files for the SOPE iCal libraries
Group:        Development/Libraries
Requires:     ogo-gnustep_make sope%{sope_major_version}%{sope_minor_version}-ical
AutoReqProv:  off

%description ical-devel
This package contains the development files of the SOPE iCal libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.
#########################################
%package gdl1
Summary:      GNUstep database libraries for SOPE
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-core sope%{sope_major_version}%{sope_minor_version}-xml libfoundation%{lfmaj}%{lfmin}
AutoReqProv:  off

%description gdl1
This package contains a fork of the GNUstep database libraries used
by the SOPE application server (including GDLContentStore).

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package gdl1-postgresql
Summary:      PostgreSQL connector for SOPE's fork of the GNUstep database environment
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-gdl1
AutoReqProv:  off
%if %{?_postgresql_server_is_within_postgresql:1}%{!?_postgresql_server_is_within_postgresql:0}
Requires: postgresql
%else
Requires: postgresql-server
%endif

%description gdl1-postgresql
This package contains the PostgreSQL connector for SOPE's fork of the
GNUstep database libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package gdl1-mysql
Summary:      MySQL connector for SOPE's fork of the GNUstep database environment
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-gdl1
AutoReqProv:  off

%description gdl1-mysql
This package contains the MySQL connector for SOPE's fork of the
GNUstep database libraries.

#%package gdl1-sqlite3
#Summary:      SQLite3 connector for SOPE's fork of the GNUstep database environment
#Group:        Development/Libraries
#Requires:     sope%{sope_major_version}%{sope_minor_version}-gdl1
#AutoReqProv:  off
#
#%description gdl1-sqlite3
#This package contains the SQLite3 connector for SOPE's fork of the
#GNUstep database libraries.
#
#SOPE is a framework for developing web applications and services. The
#name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package gdl1-tools
Summary:      Tools (gcs_cat/gcs_gensql/gcs_ls/gcs_mkdir/gcs_recreatequick)
Group:        Development/Libraries
Requires:     sope%{sope_major_version}%{sope_minor_version}-gdl1
AutoReqProv:  off

%description gdl1-tools
Various tools around the GDLContentStore.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package gdl1-devel
Summary:      Development files for the GNUstep database libraries
Group:        Development/Libraries
Requires:     ogo-gnustep_make sope%{sope_major_version}%{sope_minor_version}-gdl1 postgresql-devel
AutoReqProv:  off

%description gdl1-devel
This package contains the header files for SOPE's fork of the GNUstep
database libraries (including GDLContentStore).

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post appserver
if [ $1 = 1 ]; then
  if [ -d %{_sysconfdir}/ld.so.conf.d ]; then
    echo "%{prefix}/lib" > %{_sysconfdir}/ld.so.conf.d/sope%{sope_major_version}%{sope_minor_version}.conf
  elif [ ! "`grep '%{prefix}/lib' %{_sysconfdir}/ld.so.conf`" ]; then
    echo "%{prefix}/lib" >> %{_sysconfdir}/ld.so.conf
  fi
  /sbin/ldconfig
fi

# ****************************** postun *********************************
%postun appserver
if [ $1 = 0 ]; then
  if [ -e %{_sysconfdir}/ld.so.conf.d/sope%{sope_major_version}%{sope_minor_version}.conf ]; then
    rm -f %{_sysconfdir}/ld.so.conf.d/sope%{sope_major_version}%{sope_minor_version}.conf
  fi
  /sbin/ldconfig
fi

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
%defattr(-,root,root,-)
%{_libdir}/libDOM*.so.%{sope_libversion}*
%{_libdir}/libSaxObjC*.so.%{sope_libversion}*
%{_libdir}/libXmlRpc*.so.%{sope_libversion}*
%{_libdir}/sope-%{sope_libversion}/saxdrivers/libxmlSAXDriver.sax
%{_libdir}/sope-%{sope_libversion}/saxdrivers/STXSaxDriver.sax

%files xml-tools
%defattr(-,root,root,-)
%{_bindir}/domxml
%{_bindir}/saxxml
%{_bindir}/xmln

%files xml-devel
%defattr(-,root,root,-)
%{_includedir}/DOM
%{_includedir}/SaxObjC
%{_includedir}/XmlRpc
%{_libdir}/libDOM*.so
%{_libdir}/libSaxObjC*.so
%{_libdir}/libXmlRpc*.so

%files core
%defattr(-,root,root,-)
%{_libdir}/libEOControl*.so.%{sope_libversion}*
%{_libdir}/libNGExtensions*.so.%{sope_libversion}*
%{_libdir}/libNGStreams*.so.%{sope_libversion}*

%files core-devel
%defattr(-,root,root,-)
%{_includedir}/EOControl
%{_includedir}/NGExtensions
%{_includedir}/NGStreams
%{_libdir}/libEOControl*.so
%{_libdir}/libNGExtensions*.so
%{_libdir}/libNGStreams*.so

%files mime
%defattr(-,root,root,-)
%{_libdir}/libNGMime*.so.%{sope_libversion}*

%files mime-devel
%defattr(-,root,root,-)
%{_includedir}/NGImap4
%{_includedir}/NGMail
%{_includedir}/NGMime
%{_libdir}/libNGMime*.so

%files appserver
%defattr(-,root,root,-)
%{_libdir}/libNGObjWeb*.so.%{sope_libversion}*
%{_libdir}/libNGXmlRpc*.so.%{sope_libversion}*
%{_libdir}/libSoOFS*.so.%{sope_libversion}*
%{_libdir}/libWEExtensions*.so.%{sope_libversion}*
%{_libdir}/libWOExtensions*.so.%{sope_libversion}*
%{_libdir}/libWOXML*.so.%{sope_libversion}*
%{_datadir}/sope-%{sope_libversion}/ngobjweb/DAVPropMap.plist
%{_datadir}/sope-%{sope_libversion}/ngobjweb/Defaults.plist
%{_datadir}/sope-%{sope_libversion}/ngobjweb/Languages.plist
%{_libdir}/sope-%{sope_libversion}/products/SoCore.sxp
%{_libdir}/sope-%{sope_libversion}/products/SoOFS.sxp
%{_libdir}/sope-%{sope_libversion}/wox-builders/WEExtensions.wox
%{_libdir}/sope-%{sope_libversion}/wox-builders/WOExtensions.wox


%files appserver-tools
%defattr(-,root,root,-)
%{_sbindir}/sope-%{sope_major_version}.%{sope_minor_version}
%{_bindir}/xmlrpc_call

%files appserver-devel
%defattr(-,root,root,-)
%{_bindir}/wod
%{_includedir}/NGHttp
%{_includedir}/NGObjWeb
%{_includedir}/NGXmlRpc
%{_includedir}/SoOFS
%{_includedir}/WEExtensions
%{_includedir}/WOExtensions
%{_includedir}/WOXML
%{_libdir}/libNGObjWeb*.so
%{_libdir}/libNGXmlRpc*.so
%{_libdir}/libSoOFS*.so
%{_libdir}/libWEExtensions*.so
%{_libdir}/libWOExtensions*.so
%{_libdir}/libWOXML*.so
%{prefix}/System/Library/Makefiles/Additional/ngobjweb.make
%{prefix}/System/Library/Makefiles/woapp.make
%{prefix}/System/Library/Makefiles/wobundle.make

%files ldap
%defattr(-,root,root,-)
%{_libdir}/libNGLdap*.so.%{sope_libversion}*

%files ldap-tools
%defattr(-,root,root,-)
%{_bindir}/ldap2dsml
%{_bindir}/ldapchkpwd
%{_bindir}/ldapls

%files ldap-devel
%defattr(-,root,root,-)
%{_includedir}/NGLdap
%{_libdir}/libNGLdap*.so

%files ical
%defattr(-,root,root,-)
%{_libdir}/libNGiCal*.so.%{sope_libversion}*
%{_datadir}/sope-%{sope_libversion}/saxmappings/NGiCal.xmap
%{_libdir}/sope-%{sope_libversion}/saxdrivers/versitSaxDriver.sax

%files ical-devel
%defattr(-,root,root,-)
%{_includedir}/NGiCal
%{_libdir}/libNGiCal*.so

%files gdl1
%defattr(-,root,root,-)
%{_bindir}/connect-EOAdaptor
%{_bindir}/load-EOAdaptor
%{_libdir}/libGDLAccess*.so.%{sope_libversion}*
%{_libdir}/libGDLContentStore*.so.%{sope_libversion}*

%files gdl1-postgresql
%defattr(-,root,root,-)
%{_libdir}/sope-%{sope_libversion}/dbadaptors/PostgreSQL.gdladaptor

#%files gdl1-mysql
#%defattr(-,root,root,-)
#%{_libdir}/sope-%{sope_libversion}/dbadaptors/MySQL.gdladaptor

#%files gdl1-sqlite3
#%defattr(-,root,root,-)
#%{_libdir}/sope-%{sope_libversion}/dbadaptors/SQLite3.gdladaptor

%files gdl1-tools
%defattr(-,root,root,-)
%{_bindir}/gcs_cat
%{_bindir}/gcs_gensql
%{_bindir}/gcs_ls
%{_bindir}/gcs_mkdir
%{_bindir}/gcs_recreatequick

%files gdl1-devel
%defattr(-,root,root,-)
%{_includedir}/GDLAccess
%{_includedir}/GDLContentStore
%{_libdir}/libGDLAccess*.so
%{_libdir}/libGDLContentStore*.so
