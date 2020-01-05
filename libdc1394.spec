%define major 25
%define libname %mklibname dc1394_ %{major}
%define devname %mklibname dc1394 -d
%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Library for 1394 Digital Camera Specification
Name:		libdc1394
Version:	2.2.6
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		http://sourceforge.net/projects/libdc1394/
Source0:	http://downloads.sourceforge.net/libdc1394/%{name}-%{version}.tar.gz
Patch0:		libdc1394-2.2.0-fix-linking.patch
Patch1:		libdc1394-2.1.2-videodev.h.patch
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(sm)

%description
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

%package -n %{libname}
Summary:	Dynamic library from libdc1394
Group:		System/Libraries
Provides:	libdc1394

%description -n %{libname}
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

%package -n %{devname}
Summary:	Development components for libdc1394
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
%if "%{_lib}" != "lib"
Provides:	libdc1394-devel = %{version}-%{release}
%endif
Provides:	dc1394-devel = %{version}-%{release}

%description -n %{devname}
This archive contains the header-files for libdc1394 development

%prep
%setup -q
%apply_patches

%build
# use gcc because of VLAIS
export CC=gcc
%configure
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdc1394.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/dc1394_*
%{_includedir}/dc1394
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/*.1*

