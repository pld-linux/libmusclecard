Summary:	MuscleCard library
Summary(pl):	Biblioteka MuscleCard
Name:		libmusclecard
Version:	1.2.9
%define	bver	beta7
Release:	0.%{bver}.1
License:	BSD
Group:		Libraries
#Source0Download: http://alioth.debian.org/project/showfiles.php?group_id=30105
Source0:	http://alioth.debian.org/download.php/977/%{name}-%{version}-%{bver}.tar.gz
# Source0-md5:	7e9a6eee9f4b911529955303766e8c8f
URL:		http://www.linuxnet.com/middle.html
BuildRequires:	pcsc-lite-devel >= 1.2.9-0.beta7
Requires:	pcsc-lite >= 1.2.9-0.beta7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		muscledropdir	/usr/%{_lib}/pcsc/services

%description
MuscleCard library.

%description -l pl
Biblioteka MuscleCard.

%package devel
Summary:	Header files for MuscleCard library
Summary(pl):	Pliki nag³ówkowe biblioteki MuscleCard
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pcsc-lite-devel >= 1.2.9-0.beta7

%description devel
Header files for MuscleCard library.

%description devel -l pl
Pliki nag³ówkowe biblioteki MuscleCard.

%package static
Summary:	Static MuscleCard library
Summary(pl):	Biblioteka statyczna MuscleCard
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MuscleCard library.

%description static -l pl
Statyczna biblioteka MuscleCard.

%prep
%setup -q -n %{name}-%{version}-%{bver}

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
%{muscledropdir}
%{_mandir}/man8/bundleTool.8*

%files devel
%defattr(644,root,root,755)
%doc doc/*.pdf
%attr(755,root,root) %{_libdir}/libmusclecard.so
%{_libdir}/libmusclecard.la
%{_includedir}/PCSC/*.h
%{_pkgconfigdir}/libmusclecard.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmusclecard.a
