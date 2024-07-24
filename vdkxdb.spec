#
# Conditional build:
%bcond_without  static_libs	# static library
#
Summary:	VDKXdb - a set of data-aware widgets to build database applications using VDK
Summary(pl.UTF-8):	VDKXdb - zestaw widżetów do budowy aplikacji bazodanowych przy użyciu VDK
Name:		vdkxdb
Version:	2.5.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/vdklib/%{name}-%{version}.tar.gz
# Source0-md5:	2158d4379a57a355d75c54febd383b75
Patch0:		%{name}-xbase_ver.patch
Patch1:		%{name}-ac_FLAGS.patch
Patch2:		%{name}-link.patch
URL:		https://vdklib.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.6
BuildRequires:	vdk-devel >= 2.0
BuildRequires:	xbase-devel >= 2.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDKXdb is a set of data-aware widgets made to build light weight
database applications using VDK library.

%description -l pl.UTF-8
VDKXdb to zestaw zorientowanych na dane widżetów do budowy lekkich
aplikacji bazodanowych przy użyciu biblioteki VDK.

%package devel
Summary:	Header files for vdkxdb library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki vdkxdb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for vdkxdb library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki vdkxdb.

%package static
Summary:	Static vdkxdb library
Summary(pl.UTF-8):	Statyczna biblioteka vdkxdb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static vdkxdb library.

%description static -l pl.UTF-8
Statyczna biblioteka vdkxdb.

%package apidocs
Summary:	API documentation for vdkxdb library
Summary(pl.UTF-8):	Dokumentacja API biblioteki vdkxdb
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for vdkxdb library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki vdkxdb.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static%{!?with_static_libs:=no}
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libvdkxdb-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvdkxdb-2.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vdkxdb-config-2
%attr(755,root,root) %{_libdir}/libvdkxdb-2.so
%{_includedir}/vdkxdb-2
%{_pkgconfigdir}/vdkxdb-2.x.pc
%{_mandir}/man1/vdkxdb-config-2.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libvdkxdb-2.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/doxy/html/*.{css,html,js,png}
