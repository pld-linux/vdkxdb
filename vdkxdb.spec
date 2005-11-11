#
# Conditional build:
%bcond_without  static_libs # don't build static libraries
#
Summary:	VDKXdb - a set of data-aware widgets to build database applications using VDK
Summary(pl):	VDKXdb - zestaw wid¿etów do budowy aplikacji bazodanowych przy u¿yciu VDK
Name:		vdkxdb
Version:	2.4.0
Release:	0.1
License:	LGPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/vdklib/%{name}-%{version}.tar.gz
# Source0-md5:	e603e6f3b78bd6e17572025e02130ae7
Patch0:		%{name}-xbase_ver.patch
Patch1:		%{name}-ac_FLAGS.patch
URL:		http://vdklib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDKXdb is a set of data-aware widgets made to build light weight
database applications using VDK library.

%description -l pl
VDKXdb to zestaw zorientowanych na dane wid¿etów do budowy lekkich
aplikacji bazodanowych przy u¿yciu biblioteki VDK.

%package devel
Summary:	Header files for vdkxdb library
Summary(pl):	Pliki nag³ówkowe biblioteki vdkxdb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for vdkxdb library.

%description devel -l pl
Pliki nag³ówkowe biblioteki vdkxdb.

%package static
Summary:	Static vdkxdb library
Summary(pl):	Statyczna biblioteka vdkxdb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static vdkxdb library.

%description static -l pl
Statyczna biblioteka vdkxdb.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/doxy/html/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/vdkxdb2
%{_mandir}/man1/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
