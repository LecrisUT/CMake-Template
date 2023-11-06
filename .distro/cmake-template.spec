Name:           cmake-template
Summary:        CMake project template
Version:        0.0.0
Release:        %autorelease
License:        MIT
URL:            https://github.com/LecrisUT/CMake-Template

Source:         https://github.com/LecrisUT/CMake-Template/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  fmt-devel
BuildRequires:  catch-devel
Requires:       fmt

%description
CMake project template

%package        devel
Summary:        Development files for cmake-template
Requires:       cmake-template%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use cmake-template.


%prep
%autosetup -n cmake-template-%{version}


%build
%cmake \
    -DTEMPLATE_SHARED_LIBS=ON \
    -DTEMPLATE_TESTS=ON
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%doc README.md
%license LICENSE
%{_libdir}/libtemplate.so.*
%{_bindir}/hello

%files devel
%{_libdir}/libtemplate.so
%{_includedir}/template.h
%{_libdir}/cmake/Template
%{_libdir}/pkgconfig/template.pc


%changelog
%autochangelog
