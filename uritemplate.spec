#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : uritemplate
Version  : 3.0.1
Release  : 43
URL      : https://files.pythonhosted.org/packages/42/da/fa9aca2d866f932f17703b3b5edb7b17114bb261122b6e535ef0d9f618f8/uritemplate-3.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/42/da/fa9aca2d866f932f17703b3b5edb7b17114bb261122b6e535ef0d9f618f8/uritemplate-3.0.1.tar.gz
Summary  : URI templates
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: uritemplate-license = %{version}-%{release}
Requires: uritemplate-python = %{version}-%{release}
Requires: uritemplate-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===========
        
        Documentation_ -- GitHub_ -- Travis-CI_
        
        Simple python library to deal with `URI Templates`_. The API looks like

%package license
Summary: license components for the uritemplate package.
Group: Default

%description license
license components for the uritemplate package.


%package python
Summary: python components for the uritemplate package.
Group: Default
Requires: uritemplate-python3 = %{version}-%{release}

%description python
python components for the uritemplate package.


%package python3
Summary: python3 components for the uritemplate package.
Group: Default
Requires: python3-core
Provides: pypi(uritemplate)

%description python3
python3 components for the uritemplate package.


%prep
%setup -q -n uritemplate-3.0.1
cd %{_builddir}/uritemplate-3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609782309
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/uritemplate
cp %{_builddir}/uritemplate-3.0.1/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/uritemplate/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/uritemplate-3.0.1/LICENSE.BSD %{buildroot}/usr/share/package-licenses/uritemplate/3fe81a0fab713c08955f6d5f03aad6fcbf41b0c0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/uritemplate/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/uritemplate/3fe81a0fab713c08955f6d5f03aad6fcbf41b0c0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
