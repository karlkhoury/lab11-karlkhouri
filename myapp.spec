Name: myapp
Version: 1.0
Release: 1%{?dist}
Summary: A simple Hello World application
License: GPL
Source0: %{name}-%{version}.tar.gz

%global debug_package %{nil}

%description
A simple Hello World application.

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/share/doc/myapp
cp -a helloworld %{buildroot}/usr/local/bin/
cp -a README.md %{buildroot}/usr/share/doc/myapp/
cp -a user_guide.txt %{buildroot}/usr/share/doc/myapp/

%files
/usr/local/bin/helloworld
/usr/share/doc/myapp/README.md
/usr/share/doc/myapp/user_guide.txt

%changelog
* Wed Nov 25 2026 Karl Khouri <fredkhouri84@gmail.com> 1.0-1
- Initial package
