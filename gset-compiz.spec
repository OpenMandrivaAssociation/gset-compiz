%define name gset-compiz
%define version 0.3.4
%define subversion 0
%if %subversion
%define srcversion %{version}-%{subversion}
%else
%define srcversion %{version}
%endif
%define release %mkrel 9

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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libglade2.0-devel
BuildRequires: libGConf2-devel
BuildRequires: desktop-file-utils
BuildRequires: automake >= 1.10


%description
gset-compiz is a GTK tool to configure compiz.

%prep
%setup -q
%patch0 -p1 -b .lib_path
%patch1 -p1 -b .root
%patch2 -p1 -b .keys
%patch3 -p0 -b .automake1.10
%patch4 -p1 -b .about_close
%patch5 -p1 -b .iValue
perl -pi -e 's/\.png$//' data/%{name}.desktop

%build
aclocal; autoconf; automake; autoheader
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}%{_datadir}/%{name}/README

desktop-file-install \
  --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-Other" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/*.desktop

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/gset.glade
%{_datadir}/pixmaps/%{name}.png
