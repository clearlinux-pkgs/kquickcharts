#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kquickcharts
Version  : 5.75.0
Release  : 10
URL      : https://download.kde.org/stable/frameworks/5.75/kquickcharts-5.75.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.75/kquickcharts-5.75.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.75/kquickcharts-5.75.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 LGPL-3.0 MIT
Requires: kquickcharts-lib = %{version}-%{release}
Requires: kquickcharts-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdeclarative-dev
BuildRequires : kirigami2-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

%description
# KQuickCharts
A QtQuick module providing high-performance charts.
## Introduction

%package dev
Summary: dev components for the kquickcharts package.
Group: Development
Requires: kquickcharts-lib = %{version}-%{release}
Provides: kquickcharts-devel = %{version}-%{release}
Requires: kquickcharts = %{version}-%{release}

%description dev
dev components for the kquickcharts package.


%package lib
Summary: lib components for the kquickcharts package.
Group: Libraries
Requires: kquickcharts-license = %{version}-%{release}

%description lib
lib components for the kquickcharts package.


%package license
Summary: license components for the kquickcharts package.
Group: Default

%description license
license components for the kquickcharts package.


%prep
%setup -q -n kquickcharts-5.75.0
cd %{_builddir}/kquickcharts-5.75.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602630482
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602630482
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kquickcharts
cp %{_builddir}/kquickcharts-5.75.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kquickcharts/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kquickcharts-5.75.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kquickcharts/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kquickcharts-5.75.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kquickcharts/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kquickcharts-5.75.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kquickcharts/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kquickcharts-5.75.0/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kquickcharts/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF5QuickCharts/KF5QuickChartsConfig.cmake
/usr/lib64/cmake/KF5QuickCharts/KF5QuickChartsConfigVersion.cmake
/usr/lib64/cmake/KF5QuickCharts/KF5QuickChartsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5QuickCharts/KF5QuickChartsTargets.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/Legend.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/LegendDelegate.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/LineChartControl.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/PieChartControl.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/Theme.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/libchartscontrolsplugin.so
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/qmldir
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/styles/org.kde.desktop/Theme.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/libQuickCharts.so
/usr/lib64/qt5/qml/org/kde/quickcharts/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kquickcharts/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kquickcharts/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kquickcharts/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kquickcharts/e458941548e0864907e654fa2e192844ae90fc32
