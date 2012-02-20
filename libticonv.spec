%define major 6
%define libname %mklibname ticonv %{major}
%define develname %mklibname ticonv -d

Summary:	Communicate with TI calculators
Name:		libticonv
Version:	1.1.3
Release:	2
Group:		System/Libraries
License:	GPLv2+
URL:		http://lpg.ticalc.org/prj_tilp
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libticonv-foreign_package.patch
BuildRequires:	dos2unix
BuildRequires:	glib2-devel

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
%makeinstall_std

%files -n %{libname} 
%doc ChangeLog AUTHORS README LOGO
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/tilp2
# %{_libdir}/*.*
%{_libdir}/*.so
%{_libdir}/pkgconfig/ticonv.pc
