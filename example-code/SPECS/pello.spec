Name: pello
Version: 0.1.1
Release: alt1
Summary: Hello World example implemented in bash script
Group: Other

License: GPLv3+
URL: https://www.example.com/%{name}

Source0: https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

BuildRequires: python3
BuildArch: noarch

%add_python3_lib_path %_libexecdir/%name

%description
The long-tail description for our Hello World Example implemented in Python.

%prep
%setup -q

# fix python shebang for scripts
grep -R '^#!/usr/bin/\(env[[:space:]]\+\)\?python' . | cut -d: -f1 |
    while read f; do
        sed -E -i '1 s@^(#![[:space:]]*)%_bindir/(env[[:space:]]+)?python$@\1%__python3@' "$f"
    done

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libexecdir/%name

cat > %buildroot%_bindir/%name <<-EOF
#!/bin/bash
/usr/bin/python3 %_libexecdir%name/__pycache__/%name.cpython-$(echo %__python3_version | sed 's/\.//').pyc
EOF

chmod 0755 %buildroot%_bindir/%name

install -m 0644 %name.py %buildroot%_libexecdir/%name/

%files
%doc LICENSE
%dir %_libexecdir/%name/
%_bindir/%name
%_libexecdir/%name/%name.py
%_libexecdir/%name/__pycache__/*.py*

%changelog
* Mon Sep 05 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- First pello package
