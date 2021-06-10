#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmbox
Version  : 21.04.2
Release  : 30
URL      : https://download.kde.org/stable/release-service/21.04.2/src/kmbox-21.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.2/src/kmbox-21.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.2/src/kmbox-21.04.2.tar.xz.sig
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
BuildRequires : qtbase-dev

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
%setup -q -n kmbox-21.04.2
cd %{_builddir}/kmbox-21.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623356613
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
export SOURCE_DATE_EPOCH=1623356613
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmbox
cp %{_builddir}/kmbox-21.04.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmbox/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kmbox-21.04.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmbox/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kmbox-21.04.2/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kmbox/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kmbox-21.04.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmbox/20079e8f79713dce80ab09774505773c926afa2a
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
/usr/include/KF5/KMbox/KMbox/MBox
/usr/include/KF5/KMbox/KMbox/MBoxEntry
/usr/include/KF5/KMbox/kmbox/kmbox_export.h
/usr/include/KF5/KMbox/kmbox/mbox.h
/usr/include/KF5/KMbox/kmbox/mboxentry.h
/usr/include/KF5/kmbox_version.h
/usr/lib64/cmake/KF5Mbox/KF5MboxConfig.cmake
/usr/lib64/cmake/KF5Mbox/KF5MboxConfigVersion.cmake
/usr/lib64/cmake/KF5Mbox/KF5MboxTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Mbox/KF5MboxTargets.cmake
/usr/lib64/libKF5Mbox.so
/usr/lib64/qt5/mkspecs/modules/qt_KMbox.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Mbox.so.5
/usr/lib64/libKF5Mbox.so.5.17.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmbox/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmbox/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kmbox/8287b608d3fa40ef401339fd907ca1260c964123
