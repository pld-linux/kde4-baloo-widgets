# $Revision:$, $Date:$
%define         _state          stable
%define         orgname		baloo-widgets
%define         qtver           4.8.3

Summary:	A framework for searching and managing metadata - widgets
Name:		kde4-baloo-widgets
Version:	4.14.0
Release:	1
License:	LGPLv2 or LGPLv3
Group:		X11/Applications
URL:		http://www.kde.org/
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	89b39aa64efd7ae332ad66df63b946e6
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	akonadi-devel >= 1.12.0
BuildRequires:	kde4-baloo-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kfilemetadata-devel >= %{version}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A framework for searching and managing metadata - widgets.

%package devel
Summary:	Developer files for %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-baloo-devel >= %{version}

%description devel
Baloo widgets development files and libraries.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
		-DHTML_INSTALL_DIR=%{_kdedocdir} \
		-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
		-DKDE4_ENABLE_FINAL=OFF \
		../

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
%attr(755,root,root) %{_libdir}/libbaloowidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbaloowidgets.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/baloo/*.h
%attr(755,root,root) %{_libdir}/libbaloowidgets.so
%{_libdir}/cmake/BalooWidgets
