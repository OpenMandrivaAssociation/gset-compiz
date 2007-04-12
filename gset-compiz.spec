%define name gset-compiz
%define version 0.3.4
%define subversion 0
%if %subversion
%define srcversion %{version}-%{subversion}
%else
%define srcversion %{version}
%endif
%define release %mkrel 5

Summary: A compiz configuration tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://3v1n0.tuxfamily.org/src/%{name}-%{srcversion}.tar.bz2
Patch0:  gset-compiz-lib_path.patch
Patch1:  gset-compiz-0.3.4-root.patch
Patch2:  gset-compiz-0.3.4-keys.patch
License: GPL
Group: System/X11
Url: http://www.compiz.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libglade2.0-devel
BuildRequires: libGConf2-devel
BuildRequires: desktop-file-utils
BuildRequires: automake1.9


%description
gset-compiz is a GTK tool to configure compiz.

%prep
%setup -q
%patch0 -p1 -b .lib_path
%patch1 -p1 -b .root
%patch2 -p1 -b .keys

%build
automake-1.9
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/README

desktop-file-install \
  --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/gset.glade
%{_datadir}/pixmaps/%{name}.png


