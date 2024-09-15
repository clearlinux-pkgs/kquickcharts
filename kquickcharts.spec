#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kquickcharts
Version  : 6.6.0
Release  : 64
URL      : https://download.kde.org/stable/frameworks/6.6/kquickcharts-6.6.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.6/kquickcharts-6.6.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.6/kquickcharts-6.6.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kquickcharts-data = %{version}-%{release}
Requires: kquickcharts-lib = %{version}-%{release}
Requires: kquickcharts-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kquickcharts-6.6.0
cd %{_builddir}/kquickcharts-6.6.0
pushd ..
cp -a kquickcharts-6.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726440583
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726440583
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kquickcharts
cp %{_builddir}/kquickcharts-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kquickcharts/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kquickcharts/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kquickcharts/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kquickcharts/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kquickcharts/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kquickcharts/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kquickcharts-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kquickcharts/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kquickcharts.categories

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF6QuickCharts/KF6QuickChartsConfig.cmake
/usr/lib64/cmake/KF6QuickCharts/KF6QuickChartsConfigVersion.cmake
/usr/lib64/libQuickCharts.so
/usr/lib64/libQuickChartsControls.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQuickCharts.so.6.6.0
/V3/usr/lib64/libQuickChartsControls.so.6.6.0
/V3/usr/lib64/qt6/qml/org/kde/quickcharts/controls/libQuickChartsControlsplugin.so
/V3/usr/lib64/qt6/qml/org/kde/quickcharts/libQuickChartsplugin.so
/usr/lib64/libQuickCharts.so.1
/usr/lib64/libQuickCharts.so.6.6.0
/usr/lib64/libQuickChartsControls.so.1
/usr/lib64/libQuickChartsControls.so.6.6.0
/usr/lib64/qt6/qml/org/kde/quickcharts/QuickCharts.qmltypes
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/KirigamiTheme.qml
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/Legend.qml
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/LegendDelegate.qml
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/LineChartControl.qml
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/PieChartControl.qml
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/QuickChartsControls.qmltypes
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/Theme.qml
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/libQuickChartsControlsplugin.so
/usr/lib64/qt6/qml/org/kde/quickcharts/controls/qmldir
/usr/lib64/qt6/qml/org/kde/quickcharts/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/quickcharts/libQuickChartsplugin.so
/usr/lib64/qt6/qml/org/kde/quickcharts/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kquickcharts/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/kquickcharts/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kquickcharts/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kquickcharts/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kquickcharts/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kquickcharts/e458941548e0864907e654fa2e192844ae90fc32
