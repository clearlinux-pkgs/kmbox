#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kmbox
Version  : 19.08.2
Release  : 14
URL      : https://download.kde.org/stable/applications/19.08.2/src/kmbox-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/kmbox-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/kmbox-19.08.2.tar.xz.sig
Summary  : Library for accessing mail storages in MBox format
Group    : Development/Tools
License  : LGPL-2.1
Requires: kmbox-data = %{version}-%{release}
Requires: kmbox-lib = %{version}-%{release}
Requires: kmbox-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kmime-dev

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
%setup -q -n kmbox-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570748538
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570748538
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmbox
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kmbox/COPYING.LIB
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
/usr/lib64/qt5/mkspecs/modules/qt_Mbox.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Mbox.so.5
/usr/lib64/libKF5Mbox.so.5.12.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmbox/COPYING.LIB
