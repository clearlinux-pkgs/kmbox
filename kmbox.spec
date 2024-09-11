#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmbox
Version  : 24.08.0
Release  : 73
URL      : https://download.kde.org/stable/release-service/24.08.0/src/kmbox-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/kmbox-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/kmbox-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: kmbox-data = %{version}-%{release}
Requires: kmbox-lib = %{version}-%{release}
Requires: kmbox-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kmime-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KMBox #
KMBox provides API to access emails in storages in the [MBox](https://tools.ietf.org/html/rfc4155) format

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kmbox-24.08.0
cd %{_builddir}/kmbox-24.08.0
pushd ..
cp -a kmbox-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724649771
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
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
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
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
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
export SOURCE_DATE_EPOCH=1724649771
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmbox
cp %{_builddir}/kmbox-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/kmbox/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kmbox-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmbox/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kmbox-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmbox/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kmbox-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kmbox/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kmbox-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmbox/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kmbox-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kmbox/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/kmbox-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kmbox/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kmbox-%{version}/readme-build-ftime.txt.license %{buildroot}/usr/share/package-licenses/kmbox/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
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
/usr/share/qlogging-categories6/kmbox.categories
/usr/share/qlogging-categories6/kmbox.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KMbox/KMbox/MBox
/usr/include/KPim6/KMbox/KMbox/MBoxEntry
/usr/include/KPim6/KMbox/kmbox/kmbox_export.h
/usr/include/KPim6/KMbox/kmbox/mbox.h
/usr/include/KPim6/KMbox/kmbox/mboxentry.h
/usr/include/KPim6/KMbox/kmbox_version.h
/usr/lib64/cmake/KPim6Mbox/KPim6MboxConfig.cmake
/usr/lib64/cmake/KPim6Mbox/KPim6MboxConfigVersion.cmake
/usr/lib64/cmake/KPim6Mbox/KPim6MboxTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6Mbox/KPim6MboxTargets.cmake
/usr/lib64/libKPim6Mbox.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6Mbox.so.6.2.0
/usr/lib64/libKPim6Mbox.so.6
/usr/lib64/libKPim6Mbox.so.6.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmbox/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmbox/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kmbox/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kmbox/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kmbox/cadc9e08cb956c041f87922de84b9206d9bbffb2
