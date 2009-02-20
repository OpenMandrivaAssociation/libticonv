%define major 3
%define libname %mklibname ticonv %{major}
%define develname %mklibname ticonv -d

Summary:	Communicate with TI calculators
Name:		libticonv
Version:	1.1.0
Release:	%mkrel 4
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
