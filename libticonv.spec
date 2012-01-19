%define major 6
%define libname %mklibname ticonv %{major}
%define develname %mklibname ticonv -d

Summary:	Communicate with TI calculators
Name:		libticonv
Version:	1.1.3
Release:	%mkrel 1
Group:		System/Libraries
License:	GPLv2+
URL:		http://lpg.ticalc.org/prj_tilp
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libticonv-foreign_package.patch
BuildRequires:	dos2unix
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Communicate with TI calculators.

%package -n %{libname}
Summary:	Communicate with TI calculators
Group:		System/Libraries

%description -n %{libname}
Communicate with TI calculators.

%package -n %{develname}
Summary:	Development package for libticalcs library
Group:		Development/C
Provides:	ticonv-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname ticonv 1 -d}

%description -n %{develname}
This package contains the header files and static libraries needed to
develop applications with libticalcs.

%prep
%setup -q 
for i in ChangeLog AUTHORS README LOGO; do
    dos2unix $i
    iconv -f iso-8859-1 -t UTF-8 -o xxx $i && mv xxx $i
done

%build
%configure2_5x 

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun-n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname} 
%defattr(-,root,root)
%doc ChangeLog AUTHORS README LOGO
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/tilp2
%{_libdir}/*.*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/ticonv.pc


%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1.0-5mdv2010.0
+ Revision: 439481
- rebuild

* Fri Feb 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-4mdv2009.1
+ Revision: 343286
- add missing devel provides
- fix libification
- spec file clean

  + Zombie Ryushu <ryushu@mandriva.org>
    - Add epoch so TILP2 Drivers look different from TILP1 as suggested by Buchan

* Tue Jan 27 2009 Zombie Ryushu <ryushu@mandriva.org> 1.1.0-2mdv2009.1
+ Revision: 334043
- Fix SPEC name
- Fix SPEC name
- Obsolete old packages
- Work in progress
- Work in progress
- Work in progress
- Fix name
- Work in progress

* Mon Jan 26 2009 Zombie Ryushu <ryushu@mandriva.org> 1.1.0-1mdv2009.1
+ Revision: 333623
- New Version

* Mon Jan 26 2009 Zombie Ryushu <ryushu@mandriva.org> 1.0.5-1mdv2009.1
+ Revision: 333615
- New Version
- New Version
- import libticonv3

