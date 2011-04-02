Summary:	Qt interface for Zeitgeist
Name:		libqzeitgeist
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Libraries
URL:		http://gitorious.org/kde-zeitgeist/libqzeitgeist
#  git clone http://gitorious.org/kde-zeitgeist/libqzeitgeist
Source0:	http://gitorious.org/kde-zeitgeist/libqzeitgeist/archive-tarball/0.7#/%{name}-%{version}.tar.gz
# Source0-md5:	487ca34d75e05be0ca5dc3aee7a08003
BuildRequires:	QtDBus-devel
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Zeitgeist Library.

%package devel
Summary:	Qt Zeitgeist developement files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for Qt Zeitgeist.

%prep
%setup -q -n kde-zeitgeist-%{name}

sed -i -e 's#lib/pkgconfig#%{_lib}/pkgconfig#g' CMakeLists.txt
sed -i -e 's#${CMAKE_INSTALL_PREFIX}/lib#${CMAKE_INSTALL_PREFIX}/%{_lib}#g' src/CMakeLists.txt

%build
install -d build
cd build

%{cmake} ../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqzeitgeist.so.*.*
%ghost %attr(755,root,root) %{_libdir}/libqzeitgeist.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/QtZeitgeist
%attr(755,root,root) %{_libdir}/libqzeitgeist.so
%{_pkgconfigdir}/QtZeitgeist.pc
%{_datadir}/qzeitgeist
