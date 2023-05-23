#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kquickcharts
Version  : 5.106.0
Release  : 40
URL      : https://download.kde.org/stable/frameworks/5.106/kquickcharts-5.106.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.106/kquickcharts-5.106.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.106/kquickcharts-5.106.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kquickcharts-data = %{version}-%{release}
Requires: kquickcharts-lib = %{version}-%{release}
Requires: kquickcharts-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdeclarative-dev
BuildRequires : kirigami2-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KQuickCharts
A QtQuick module providing high-performance charts.
## Introduction

%package data
Summary: data components for the kquickcharts package.
Group: Data

%description data
data components for the kquickcharts package.


%package dev
Summary: dev components for the kquickcharts package.
Group: Development
Requires: kquickcharts-lib = %{version}-%{release}
Requires: kquickcharts-data = %{version}-%{release}
Provides: kquickcharts-devel = %{version}-%{release}
Requires: kquickcharts = %{version}-%{release}

%description dev
dev components for the kquickcharts package.


%package lib
Summary: lib components for the kquickcharts package.
Group: Libraries
Requires: kquickcharts-data = %{version}-%{release}
Requires: kquickcharts-license = %{version}-%{release}

%description lib
lib components for the kquickcharts package.


%package license
Summary: license components for the kquickcharts package.
Group: Default

%description license
license components for the kquickcharts package.


%prep
%setup -q -n kquickcharts-5.106.0
cd %{_builddir}/kquickcharts-5.106.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684812642
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1684812642
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kquickcharts
cp %{_builddir}/kquickcharts-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kquickcharts/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kquickcharts/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kquickcharts/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kquickcharts/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kquickcharts/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kquickcharts/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kquickcharts/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kquickcharts.categories

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF5QuickCharts/KF5QuickChartsConfig.cmake
/usr/lib64/cmake/KF5QuickCharts/KF5QuickChartsConfigVersion.cmake

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/qml/org/kde/quickcharts/controls/libQuickChartsControls.so
/V3/usr/lib64/qt5/qml/org/kde/quickcharts/libQuickCharts.so
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/Legend.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/LegendDelegate.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/LineChartControl.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/Logging.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/PieChartControl.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/Theme.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/libQuickChartsControls.so
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/qmldir
/usr/lib64/qt5/qml/org/kde/quickcharts/controls/styles/org.kde.desktop/Theme.qml
/usr/lib64/qt5/qml/org/kde/quickcharts/libQuickCharts.so
/usr/lib64/qt5/qml/org/kde/quickcharts/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kquickcharts/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/kquickcharts/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kquickcharts/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kquickcharts/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kquickcharts/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kquickcharts/e458941548e0864907e654fa2e192844ae90fc32
