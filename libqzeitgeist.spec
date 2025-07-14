Summary:	Qt interface for Zeitgeist service
Summary(pl.UTF-8):	Interfejs Qt do usługi Zeitgeist
Name:		libqzeitgeist
Version:	0.8.0
Release:	5
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/libqzeitgeist/0.8.0/src/%{name}-%{version}.tar.bz2
# Source0-md5:	97bdea6a1865db7d5f29c93e3a492f24
Patch0:		%{name}-cmake.patch
URL:		https://projects.kde.org/projects/kdesupport/libqzeitgeist/
BuildRequires:	QtCore-devel >= 4.7.0
BuildRequires:	QtDBus-devel >= 4.7.0
BuildRequires:	QtDeclarative-devel >= 4.7.0
BuildRequires:	QtGui-devel >= 4.7.0
BuildRequires:	QtTest-devel >= 4.7.0
BuildRequires:	cmake >= 2.8.6
BuildRequires:	python-zeitgeist >= 0.8
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.603
Requires:	QtCore >= 4.7.0
Requires:	QtDBus >= 4.7.0
Requires:	QtGui >= 4.7.0
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

%package -n QtDeclarative-plugin-qzeitgeist
Summary:	Qt Zeitgeist plugin for QtDeclarative
Summary(pl.UTF-8):	Wtyczka Qt Zeitgeist dla QtDeclarative
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtDeclarative >= 4.7.0

%description -n QtDeclarative-plugin-qzeitgeist
Qt Zeitgeist plugin for QtDeclarative.

%description -n QtDeclarative-plugin-qzeitgeist -l pl.UTF-8
Wtyczka Qt Zeitgeist dla QtDeclarative.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake ..
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
%attr(755,root,root) %{_libdir}/libqzeitgeist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqzeitgeist.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqzeitgeist.so
%{_includedir}/QZeitgeist
%{_pkgconfigdir}/QZeitgeist.pc
%{_libdir}/cmake/QZeitgeist

%files -n QtDeclarative-plugin-qzeitgeist
%defattr(644,root,root,755)
%dir %{_libdir}/qt4/imports/org/gnome
%dir %{_libdir}/qt4/imports/org/gnome/zeitgeist
%attr(755,root,root) %{_libdir}/qt4/imports/org/gnome/zeitgeist/libQZeitgeistDeclarativePlugin.so
%{_libdir}/qt4/imports/org/gnome/zeitgeist/qmldir
