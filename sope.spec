# sRevision: 1.4 $, $Date: 2004-11-21 21:08:17 $
Summary:	WebObjects 4.x compatible library with extensions
Summary(pl):	Biblioteka kompatybilna z WebObjects 4.x
Name:		sope
Version:	4.3.9
%define rel 301
Release:	%{rel}.1
License:	LGPL
Group:		Libraries
Source0:	http://download.opengroupware.org/sources/releases/%{name}-%{version}-shapeshifter-r%{rel}.tar.gz
# Source0-md5:	8a1ed22c46523048666318cc2f33de68
URL:		http://sope.opengroupware.org
BuildRequires:	gnustep-db-devel
BuildRequires:	gnustep-base-devel
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
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
The SOPE package is an extensive set of frameworks (16 frameworks, ~1500 classes) which form a complete Web application server environment. Besides the Apple WebObjects  compatible appserver extended with Zope  concepts, it contains a large set of reusable classes: XML processing (SAX2, DOM, XML-RPC), MIME/IMAP4 processing, LDAP connectivity, RDBMS connectivity, and iCalendar parsing.

The individual frameworks of the package can be used standalone (for example in Cocoa applications) and do not require the application server itself. 

%package devel
Summary:	Header files for sope library
Summary(pl):	Pliki nag³ówkowe biblioteki sope
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for sope library.

%description devel -l pl
Pliki nag³ówkowe biblioteki sope.

%package EOF
Summary:	Enterprise Objects Framework
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description EOF
Enterprise Objects Framework.

%package EOF-devel
Summary:	Headers for Enterprise Objects Framework
Group:		Development/Libraries
Requires:	%{name}-EOF = %{version}-%{release}

%description EOF-devel
Headers for Enterprise Objects Framework.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_prefix}/System/Library/GDLAdaptors-1.1
%dir %{_prefix}/System/Library/GDLAdaptors-1.1/*.gdladaptor/
%dir %{_prefix}/System/Library/GDLAdaptors-1.1/*.gdladaptor/Resources/
%{_prefix}/System/Library/GDLAdaptors-1.1/*.gdladaptor/Resources/*.plist
%dir %{_prefix}/System/Library/GDLAdaptors-1.1/*.gdladaptor/Resources/Version
%dir %{_prefix}/System/Library/GDLAdaptors-1.1/*.gdladaptor/%{gscpu}
%dir %{_prefix}/System/Library/GDLAdaptors-1.1/*.gdladaptor/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/GDLAdaptors-1.1/*.gdladaptor/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Library/GDLAdaptors-1.1/*.gdladaptor/%{gscpu}/%{gsos}/%{libcombo}/*
%dir %{_prefix}/System/Library/Libraries/Resources/NGObjWeb
%{_prefix}/System/Library/Libraries/Resources/NGObjWeb/*.plist
%dir %{_prefix}/System/Library/Libraries/%{gscpu}
%dir %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libDOM.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libGDLAccess.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGExtensions.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGiCal.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGLdap.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGMime.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGObjWeb.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGStreams.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libNGXmlRpc.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libSaxObjC.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libSoOFS.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libWEExtensions.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libWOExtensions.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libWOXML.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libXmlRpc.so.*
%dir %{_prefix}/System/Library/SaxDrivers-4.3
%dir %{_prefix}/System/Library/SaxDrivers-4.3/*.sax/
%{_prefix}/System/Library/SaxDrivers-4.3/*.sax/*.plist
%dir %{_prefix}/System/Library/SaxDrivers-4.3/*.sax/Resources/
%{_prefix}/System/Library/SaxDrivers-4.3/*.sax/Resources/*.plist
%{_prefix}/System/Library/SaxDrivers-4.3/*.sax/Resources/Version
%dir %{_prefix}/System/Library/SaxDrivers-4.3/*.sax/%{gscpu}
%dir %{_prefix}/System/Library/SaxDrivers-4.3/*.sax/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/SaxDrivers-4.3/*.sax/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Library/SaxDrivers-4.3/*.sax/%{gscpu}/%{gsos}/%{libcombo}/*
%dir %{_prefix}/System/Library/SaxMappings
%{_prefix}/System/Library/SaxMappings/*.xmap
%dir %{_prefix}/System/Library/SoProducts-4.3
%dir %{_prefix}/System/Library/SoProducts-4.3/*.sxp
%dir %{_prefix}/System/Library/SoProducts-4.3/*.sxp/Resources
%{_prefix}/System/Library/SoProducts-4.3/*.sxp/Resources/*.plist
%{_prefix}/System/Library/SoProducts-4.3/*.sxp/Resources/Version
%dir %{_prefix}/System/Library/SoProducts-4.3/*.sxp/%{gscpu}
%dir %{_prefix}/System/Library/SoProducts-4.3/*.sxp/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/SoProducts-4.3/*.sxp/%{gscpu}/%{gsos}/%{libcombo}
%{_prefix}/System/Library/SoProducts-4.3/*.sxp/%{gscpu}/%{gsos}/%{libcombo}/*
%dir %{_prefix}/System/Library/WOxElemBuilders-4.3
%dir %{_prefix}/System/Library/WOxElemBuilders-4.3/*.wox
%{_prefix}/System/Library/WOxElemBuilders-4.3/*.wox/*.plist
%dir %{_prefix}/System/Library/WOxElemBuilders-4.3/*.wox/Resources
%{_prefix}/System/Library/WOxElemBuilders-4.3/*.wox/Resources/*.plist
%dir %{_prefix}/System/Library/WOxElemBuilders-4.3/*.wox/%{gscpu}
%dir %{_prefix}/System/Library/WOxElemBuilders-4.3/*.wox/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/WOxElemBuilders-4.3/*.wox/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Library/WOxElemBuilders-4.3/*.wox/%{gscpu}/%{gsos}/%{libcombo}/*
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/*


%files devel
%{_prefix}/System/Library/Makefiles/Additional/*.make
%{_prefix}/System/Library/Makefiles/*.make
%{_prefix}/System/Library/Headers/%{libcombo}/DOM/
%{_prefix}/System/Library/Headers/%{libcombo}/GDLAccess/
%{_prefix}/System/Library/Headers/%{libcombo}/NGExtensions/
%{_prefix}/System/Library/Headers/%{libcombo}/NGHttp/
%{_prefix}/System/Library/Headers/%{libcombo}/NGiCal/
%{_prefix}/System/Library/Headers/%{libcombo}/NGImap4/
%{_prefix}/System/Library/Headers/%{libcombo}/NGLdap/
%{_prefix}/System/Library/Headers/%{libcombo}/NGMail/
%{_prefix}/System/Library/Headers/%{libcombo}/NGMime/
%{_prefix}/System/Library/Headers/%{libcombo}/NGObjWeb/
%{_prefix}/System/Library/Headers/%{libcombo}/NGStreams/
%{_prefix}/System/Library/Headers/%{libcombo}/NGXmlRpc/
%{_prefix}/System/Library/Headers/%{libcombo}/SaxObjC/
%{_prefix}/System/Library/Headers/%{libcombo}/SoOFS/
%{_prefix}/System/Library/Headers/%{libcombo}/WEExtensions/
%{_prefix}/System/Library/Headers/%{libcombo}/WOExtensions/
%{_prefix}/System/Library/Headers/%{libcombo}/WOXML/
%{_prefix}/System/Library/Headers/%{libcombo}/XmlRpc/

%files EOF
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libEO*.so.*

%files EOF-devel
%{_prefix}/System/Library/Headers/%{libcombo}/EOControl
