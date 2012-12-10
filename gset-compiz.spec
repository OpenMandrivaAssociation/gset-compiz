%define name gset-compiz
%define version 0.3.4
%define subversion 0
%if %subversion
%define srcversion %{version}-%{subversion}
%else
%define srcversion %{version}
%endif
%define release 11

Summary: A compiz configuration tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://3v1n0.tuxfamily.org/src/%{name}-%{srcversion}.tar.bz2
Patch0:  gset-compiz-lib_path.patch
Patch1:  gset-compiz-0.3.4-root.patch
Patch2:  gset-compiz-0.3.4-keys.patch
Patch3:  gset-compiz-automake1.10.diff
Patch4:	 gset-compiz-0.3.4-about_close.patch
Patch5:	 gset-compiz-0.3.4-iValue.patch
License: GPL
Group: System/X11
Url: http://www.compiz.net/
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: desktop-file-utils
BuildRequires: automake >= 1.10


%description
gset-compiz is a GTK tool to configure compiz.

%prep
%setup -q
#% patch0 -p1 -b .lib_path
%patch1 -p1 -b .root
%patch2 -p1 -b .keys
%patch3 -p0 -b .automake1.10
%patch4 -p1 -b .about_close
%patch5 -p1 -b .iValue
perl -pi -e 's/\.png$//' data/%{name}.desktop
chmod go+r src/gset.c

%build
export LIBS="-l X11"
aclocal; autoconf; automake; autoheader
%configure2_5x
%make

%install
%makeinstall
rm -f %{buildroot}%{_datadir}/%{name}/README

desktop-file-install \
  --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-Other" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/gset.glade
%{_datadir}/pixmaps/%{name}.png


%changelog
* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3.4-11mdv2009.0
+ Revision: 246654
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Mar 03 2008 Olivier Blin <oblin@mandriva.com> 0.3.4-9mdv2008.1
+ Revision: 178019
- fix crash (#36028, wobbly fx values are now integers and not strings)

* Mon Mar 03 2008 Olivier Blin <oblin@mandriva.com> 0.3.4-8mdv2008.1
+ Revision: 177825
- remove icon extension in desktop file
- fix about dialog not closing (#25571)
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-7mdv2008.0
+ Revision: 75300
- fix build
- fix build


* Thu Sep 21 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-21 15:11:02 (62512)
- buildrequires desktop-file-utils

* Thu Sep 21 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-21 15:04:15 (62511)
- buildrequires libGConf2-devel

* Thu Sep 21 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-21 13:57:48 (62503)
- fix gconf keys for shortcuts (#24772)

* Wed Sep 20 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-20 18:35:23 (62470)
- 0.3.4-3mdv

* Wed Sep 20 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-20 18:34:42 (62469)
- buildrequire libglade2.0-devel, not libglade-devel

* Wed Sep 20 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-20 18:09:16 (62465)
- modify system gconf settings when running gset-compiz as root

* Wed Aug 30 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-30 00:14:00 (58753)
- 0.3.4

* Sat Aug 26 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-26 14:23:57 (58176)
- add Mandriva menu category (#24775)

* Thu Aug 24 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-24 18:25:35 (57922)
- fix plugins path on x86_64

* Thu Aug 24 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-24 14:45:10 (57842)
- buildrequires libglade-devel (thanks Iurt)

* Thu Aug 24 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-24 14:42:48 (57841)
- Import gset-compiz

* Sat Aug 19 2006 Olivier Blin <blino@mandriva.com> 0.3.3-1mdv2007.0
- initial Mandriva release

