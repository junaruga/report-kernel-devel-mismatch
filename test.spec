Name: test
Version: 1
Release: 1%{?dist}
Summary: Test
License: Public Domain
URL: https://github.com/junaruga/report-kernel-devel-mismatch
BuildRequires: kernel-devel

%description

%prep
cat > hello.sh <<EOF
#!/bin/bash
echo "Hello."
EOF

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 hello.sh %{buildroot}/%{_bindir}/hello.sh

%check
uname -r
rpm -q kernel-devel
# Check if there is the kernel-devel that is the same version with the running
# kernel.
rpm -q kernel-devel | grep -q "^kernel-devel-$(uname -r)$"

%files
%{_bindir}/hello.sh

%changelog
* Wed Jan 29 2025 Jun Aruga <jaruga@redhat.com> - 1-1
- Init.
