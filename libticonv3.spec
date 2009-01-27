%define major 3
%define libname %mklibname ticonv %{major}
%define develname %mklibname ticonv -d
Name:           libticonv
BuildRequires:  pkgconfig dos2unix glib2-devel
Summary:        Communicate with TI calculators
Version:        1.1.0
Release:        %mkrel 1
Group:          System/Libraries
License:        GNU General Public License (GPL)
URL:            http://lpg.ticalc.org/prj_tilp
Source:         %{name}-%{version}.tar.bz2
Patch0:         libticonv-foreign_package.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Obsoletes:	libticonv3

%define doc_files ChangeLog AUTHORS README LOGO

%description
Communicate with TI calculators.

%package -n %{libname}
Summary:        Communicate with TI calculators
Group:          System/Libraries
Obsoletes:	libticonv3

%description -n %{libname}
Communicate with TI calculators.

%package -n %{develname}
Summary:        Development package for libticalcs library
Group:          Development/C
Requires:       %{libname} glib2-devel
Obsoletes:	libticonv3-devel

%description -n %{develname}
This package contains the header files and static libraries needed to
develop applications with libticalcs.



%prep
%setup -q -n libticonv-%{version}
for i in %{doc_files}; do
    dos2unix $i
    iconv -f iso-8859-1 -t UTF-8 -o xxx $i && mv xxx $i
done

%build
autoreconf -fi
export CFLAGS="%{optflags}" 
./configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}
make

%install
%makeinstall

%post
ldconfig

%postun
ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname} 
%defattr(-,root,root)
%doc %{doc_files}
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/tilp2
%{_libdir}/*.*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/ticonv.pc

