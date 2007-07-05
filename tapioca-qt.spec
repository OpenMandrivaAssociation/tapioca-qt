%define lib_name_orig %mklibname %name
%define lib_major 0
%define lib_name %lib_name_orig%lib_major
%define oname Tapioca-Qt

Name:          tapioca-qt
Version:       0.14.1
Release:       %mkrel 1
Summary:       High-level classes on top of TelepathyQt for use in clients
License:       GPL
Group:         Networking/Instant messaging
Url:           http://telepathy.freedesktop.org/wiki/TapiocaQt
Source:        %name-%version.tar.bz2 
Patch0:        tapioca-qt-fix_x86_64.patch 
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: libtelepathy-qt-devel

Provides:      TapiocaQt

%description
Tapioca-qt is a Qt4 package containing high-level classes on
top of TelepathyQt for use in clients. It's used in at least 
decibel and kopete experimental telepathy branch.

#---------------------------------------------------------------------

%package -n %lib_name
Summary:        Headers files for %{name}
Group:          Development/Other
Provides:       libtapioca-qt

%description -n %lib_name
%oname is a Qt4 package containing high-level classes on 
top of TelepathyQt for use in clients. 

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root)
%_libdir/libQtTapioca.so.0
%_libdir/libQtTapioca.so.0.1.0

#--------------------------------------------------------------------

%package  -n %lib_name-devel
Requires:       %{lib_name} = %{version}
Summary:        %{oname} development files
Group:          Development/Other
Provides:       libtapioca-qt-devel

%description -n %lib_name-devel
Tapioca-qt development files.

%files  -n %lib_name-devel
%defattr(-,root,root)
%_includedir/QtTapioca/Avatar
%_includedir/QtTapioca/CMakeLists.txt
%_includedir/QtTapioca/Channel
%_includedir/QtTapioca/ChannelTarget
%_includedir/QtTapioca/Connection
%_includedir/QtTapioca/ConnectionManager
%_includedir/QtTapioca/ConnectionManagerFactory
%_includedir/QtTapioca/Contact
%_includedir/QtTapioca/ContactBase
%_includedir/QtTapioca/ContactList
%_includedir/QtTapioca/DBusProxyObject
%_includedir/QtTapioca/Handle
%_includedir/QtTapioca/HandleFactory
%_includedir/QtTapioca/TextChannel
%_includedir/QtTapioca/UserContact
%_includedir/QtTapioca/avatar.h
%_includedir/QtTapioca/channel.h
%_includedir/QtTapioca/channeltarget.h
%_includedir/QtTapioca/connection.h
%_includedir/QtTapioca/connectionmanager.h
%_includedir/QtTapioca/connectionmanagerfactory.h
%_includedir/QtTapioca/contact.h
%_includedir/QtTapioca/contactbase.h
%_includedir/QtTapioca/contactlist.h
%_includedir/QtTapioca/dbusproxyobject.h
%_includedir/QtTapioca/handle.h
%_includedir/QtTapioca/handlefactory.h
%_includedir/QtTapioca/textchannel.h
%_includedir/QtTapioca/usercontact.h
%_includedir/QtTapioca/Stream
%_includedir/QtTapioca/StreamChannel
%_includedir/QtTapioca/stream.h
%_includedir/QtTapioca/streamchannel.h

%_libdir/libQtTapioca.so
%_libdir/pkgconfig/QtTapioca.pc

#--------------------------------------------------------------------

%prep

%setup -q -n %name 
#%patch0 -p1 -b .fix_x86_64
%build


cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        %if "%{_lib}" != "lib"
                -DLIB_SUFFIX=64 \
        %endif
        -DQT_QMAKE_EXECUTABLE=/usr/lib/qt4/bin/qmake

%install
rm -fr %buildroot
make DESTDIR=%buildroot  install



