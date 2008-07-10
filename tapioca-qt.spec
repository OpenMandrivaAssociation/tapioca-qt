%define revision 829319

Name: tapioca-qt
Version: 0.17.7
Release: %mkrel 0.%revision.1
Epoch: 1
Summary: High-level classes on top of TelepathyQt for use in clients
License: GPL
Group: Networking/Instant messaging
Url: http://telepathy.freedesktop.org/wiki/TapiocaQt
Source: %name-%version.%revision.tar.bz2 
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: telepathy-qt-devel

%description
Tapioca-qt is a Qt4 package containing high-level classes on
top of TelepathyQt for use in clients. It's used in at least 
decibel and kopete experimental telepathy branch.

#---------------------------------------------------------------------

%define libQtTapioca %mklibname QtTapioca 0

%package -n %libQtTapioca
Summary: %{name} core library
Group: System/Libraries
Obsoletes: %{_lib}tapioca-qt0

%description -n %libQtTapioca
%name core library.

%if %mdkversion < 200900
%post -n %libQtTapioca -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libQtTapioca -p /sbin/ldconfig
%endif

%files -n %libQtTapioca
%defattr(-,root,root)
%_libdir/libQtTapioca.so.*

#--------------------------------------------------------------------

%package devel
Requires: %libQtTapioca = %{epoch}:%{version}
Summary: %name development files
Group: Development/Other
Provides: libtapioca-qt-devel
Obsoletes: %{_lib}tapioca-qt0-devel

%description devel
Tapioca-qt development files.

%files devel
%defattr(-,root,root)
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/QtTapioca.pc

#--------------------------------------------------------------------

%prep
%setup -q 
%build
%cmake_qt4

%make

%install
rm -fr %buildroot

cd build
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot

