Summary:	Qt interface for Zeitgeist service
Summary(pl.UTF-8):	Interfejs Qt do usługi Zeitgeist
Name:		libqzeitgeist
Version:	0.7
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# git clone http://gitorious.org/kde-zeitgeist/libqzeitgeist
Source0:	http://gitorious.org/kde-zeitgeist/libqzeitgeist/archive-tarball/0.7#/%{name}-%{version}.tar.gz
# Source0-md5:	487ca34d75e05be0ca5dc3aee7a08003
URL:		http://gitorious.org/kde-zeitgeist/libqzeitgeist
BuildRequires:	QtCore-devel >= 4.7.0
BuildRequires:	QtDBus-devel >= 4.7.0
BuildRequires:	QtTest-devel >= 4.7.0
BuildRequires:	cmake >= 2.6
BuildRequires:	rpmbuild(macros) >= 1.603
BuildRequires:	sed >= 4.0
Requires:	QtCore >= 4.7.0
Requires:	QtDBus >= 4.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Zeitgeist library, providing access to Zeitgeist service.

%description -l pl.UTF-8
Biblioteka Qt Zeitgeist, dająca dostęp do usługi Zeitgeist.

%package devel
Summary:	Qt Zeitgeist development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Qt Zeitgeist
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.7.0
Requires:	QtDBus-devel >= 4.7.0

%description devel
Development files for Qt Zeitgeist library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki Qt Zeitgeist.

%prep
%setup -q -n kde-zeitgeist-%{name}

sed -i -e 's#lib/pkgconfig#%{_lib}/pkgconfig#g' CMakeLists.txt
sed -i -e 's#${CMAKE_INSTALL_PREFIX}/lib#${CMAKE_INSTALL_PREFIX}/%{_lib}#g' src/CMakeLists.txt

%build
install -d build
cd build
%cmake ../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqzeitgeist.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libqzeitgeist.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqzeitgeist.so
%{_includedir}/QtZeitgeist
%{_pkgconfigdir}/QtZeitgeist.pc
%{_datadir}/qzeitgeist
