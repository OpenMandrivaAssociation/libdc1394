%define major 22
%define libname %mklibname dc1394_ %{major}
%define develname %mklibname dc1394 -d

Summary:	Library for 1394 Digital Camera Specification
Name:		libdc1394
Version:	2.2.1
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://sourceforge.net/projects/libdc1394/
Source0:	http://downloads.sourceforge.net/libdc1394/%{name}-%{version}.tar.gz
Patch1:		libdc1394-2.1.2-videodev.h.patch
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libv4l2)
Requires:	libraw1394

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

%package -n %{develname}
Summary:	Development components for libdc1394
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
%if "%{_lib}" != "lib"
Provides:	libdc1394-devel = %{version}-%{release}
%endif
Provides:	dc1394-devel = %{version}-%{release}

%description -n %{develname}
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

This archive contains the header-files for libdc1394 development

%prep
%setup -q
%patch1 -p0 -b .v4l

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/dc1394_vloopback
%{_bindir}/dc1394_reset_bus
%{_includedir}/dc1394
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/*.1*

%changelog
* Mon Jun 18 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2.1.3-2
- Add patch2 to fix Digikam crash

* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 2.1.3-1mdv2011.0
+ Revision: 672677
- new version 2.1.3

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 2.1.2-7
+ Revision: 662434
- fix build with latest cooker

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 2.1.2-6
+ Revision: 636025
- rebuild
- tighten BR

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.2-5mdv2011.0
+ Revision: 602535
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.2-4mdv2010.1
+ Revision: 520762
- rebuilt for 2010.1

* Tue Sep 22 2009 Thierry Vignaud <tv@mandriva.org> 2.1.2-3mdv2010.0
+ Revision: 447448
- use libusb1

  + Götz Waschk <waschk@mandriva.org>
    - don't obsolete old devel package

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 2.1.2-1mdv2010.0
+ Revision: 447424
- patch to fix build
- new version
- update source URL
- fix build

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.3-3mdv2010.0
+ Revision: 423702
- rebuild

  + Emmanuel Andry <eandry@mandriva.org>
    - New version
    - drop patches
    - new major
    - protect major
    - enable parallel build
    - update file list

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-6mdv2009.0
+ Revision: 222533
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-5mdv2008.1
+ Revision: 150549
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-4mdv2008.0
+ Revision: 76780
- new devel naming
- reconstruct the autofoo toolchain


* Wed Feb 14 2007 Götz Waschk <waschk@mandriva.org> 1.2.1-3mdv2007.0
+ Revision: 120708
- Import libdc1394

* Wed Feb 14 2007 Götz Waschk <waschk@mandriva.org> 1.2.1-3mdv2007.1
- use the right configure macro
- unpack patch
- additional devel provides

* Sun Sep 10 2006 Emmanuel Andry <eandry@mandriva.com> 1.2.1-2mdv2007.0
- disable // build

* Sun Jul 02 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.1-1mdv2007.0
- 1.2.1
- new major
- replace deprecated CLK_TCK with CLOCKS_PER_SEC (P1)
- remove COPYING & INSTALL from %%doc

* Tue Dec 27 2005 Stefan van der Eijk <stefan@eijk.nu> 1.1.0-1mdk
- 1.1.0
- %%mkrel

* Sun Jan 30 2005 Austin Acton <austin@mandrake.org> 1.0.0-2mdk
- rebuild for libraw1394

* Fri Nov 12 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.0-1mdk
- 1.0.0
- new major (old one incorrect btw.?)

* Tue Sep 21 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.9.5-2mdk
- lib64 fixes

* Thu Jul 15 2004 Nicolas Planel <nplanel@mandrakesoft.com> 0.9.5-1mdk
- 0.9.5
- fix bad char in Requires.

* Sun Jun 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.4-1mdk
- 0.9.4

