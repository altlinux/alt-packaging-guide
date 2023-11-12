Name: bello
Version: 0.1
Release: alt1
Summary: Hello World example implemented in bash script
Group: Other

License: GPLv3+
URL: https://www.example.com/%{name}

Source0: https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

Requires: bash
BuildArch: noarch

%description
The long-tail description for our Hello World Example implemented in
bash script.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_bindir

install -m 0755 %name %buildroot%_bindir/%name

%files
%doc LICENSE
%_bindir/%name

%changelog
* Mon Sep 05 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1-alt1
- First bello package
