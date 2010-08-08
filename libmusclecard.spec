Summary:	MuscleCard library
Summary(pl.UTF-8):	Biblioteka MuscleCard
Name:		libmusclecard
Version:	1.3.6
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: http://alioth.debian.org/project/showfiles.php?group_id=30105
Source0:	http://alioth.debian.org/download.php/3024/%{name}-%{version}.tar.gz
# Source0-md5:	f8d799b03b810f6c1238063a85a268a1
URL:		http://www.linuxnet.com/middle.html
BuildRequires:	pcsc-lite-devel >= 1.3.0
BuildRequires:	pkgconfig
Requires:	pcsc-lite >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		muscledropdir	/usr/%{_lib}/pcsc/services

%description
MuscleCard library.

%description -l pl.UTF-8
Biblioteka MuscleCard.

%package devel
Summary:	Header files for MuscleCard library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki MuscleCard
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pcsc-lite-devel >= 1.3.0

%description devel
Header files for MuscleCard library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki MuscleCard.

%package static
Summary:	Static MuscleCard library
Summary(pl.UTF-8):	Biblioteka statyczna MuscleCard
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MuscleCard library.

%description static -l pl.UTF-8
Statyczna biblioteka MuscleCard.

%prep
%setup -q

%build
%configure \
	--enable-muscledropdir=%{muscledropdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{muscledropdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog* README
%attr(755,root,root) %{_sbindir}/bundleTool
%attr(755,root,root) %{_libdir}/libmusclecard.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmusclecard.so.1
%{muscledropdir}
%{_mandir}/man8/bundleTool.8*

%files devel
%defattr(644,root,root,755)
%doc doc/muscle-api-1.3.0.pdf
%attr(755,root,root) %{_libdir}/libmusclecard.so
%{_libdir}/libmusclecard.la
%{_includedir}/PCSC/mscdefines.h
%{_includedir}/PCSC/musclecard.h
%{_pkgconfigdir}/libmusclecard.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmusclecard.a
