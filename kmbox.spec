#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmbox
Version  : 23.04.0
Release  : 52
URL      : https://download.kde.org/stable/release-service/23.04.0/src/kmbox-23.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.0/src/kmbox-23.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.0/src/kmbox-23.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: kmbox-data = %{version}-%{release}
Requires: kmbox-lib = %{version}-%{release}
Requires: kmbox-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kmime-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

%package data
Summary: data components for the kmbox package.
Group: Data

%description data
data components for the kmbox package.


%package dev
Summary: dev components for the kmbox package.
Group: Development
Requires: kmbox-lib = %{version}-%{release}
Requires: kmbox-data = %{version}-%{release}
Provides: kmbox-devel = %{version}-%{release}
Requires: kmbox = %{version}-%{release}

%description dev
dev components for the kmbox package.


%package lib
Summary: lib components for the kmbox package.
Group: Libraries
Requires: kmbox-data = %{version}-%{release}
Requires: kmbox-license = %{version}-%{release}

%description lib
lib components for the kmbox package.


%package license
Summary: license components for the kmbox package.
Group: Default

%description license
license components for the kmbox package.


%prep
%setup -q -n kmbox-23.04.0
cd %{_builddir}/kmbox-23.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682107428
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1682107428
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmbox
cp %{_builddir}/kmbox-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/kmbox/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kmbox-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmbox/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kmbox-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmbox/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kmbox-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kmbox/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kmbox-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmbox/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kmbox-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kmbox/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/kmbox-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kmbox/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kmbox.categories
/usr/share/qlogging-categories5/kmbox.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim5/KMbox/KMbox/MBox
/usr/include/KPim5/KMbox/KMbox/MBoxEntry
/usr/include/KPim5/KMbox/kmbox/kmbox_export.h
/usr/include/KPim5/KMbox/kmbox/mbox.h
/usr/include/KPim5/KMbox/kmbox/mboxentry.h
/usr/include/KPim5/KMbox/kmbox_version.h
/usr/lib64/cmake/KF5Mbox/KF5MboxConfig.cmake
/usr/lib64/cmake/KF5Mbox/KF5MboxConfigVersion.cmake
/usr/lib64/cmake/KF5Mbox/KPim5MboxTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Mbox/KPim5MboxTargets.cmake
/usr/lib64/cmake/KPim5Mbox/KPim5MboxConfig.cmake
/usr/lib64/cmake/KPim5Mbox/KPim5MboxConfigVersion.cmake
/usr/lib64/cmake/KPim5Mbox/KPim5MboxTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5Mbox/KPim5MboxTargets.cmake
/usr/lib64/libKPim5Mbox.so
/usr/lib64/qt5/mkspecs/modules/qt_KMbox.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKPim5Mbox.so.5
/usr/lib64/libKPim5Mbox.so.5.23.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmbox/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmbox/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kmbox/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kmbox/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kmbox/cadc9e08cb956c041f87922de84b9206d9bbffb2
