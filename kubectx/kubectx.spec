Name:           kubectx
Version:        0.9.5
Release:        1%{?dist}
Summary:        The Kubernetes context manager

License:        Apache License 2.0
URL:            https://github.com/ahmetb/kubectx
Source0:        https://github.com/ahmetb/kubectx/releases/download/v%{version}/kubectx_v%{version}_linux_x86_64.tar.gz

Requires:       bash

%global debug_package %{nil}

%description
Kubernetes context manager for bash and zsh.

%prep
%autosetup -c

%install
mkdir -p %{buildroot}/%{_bindir}
chmod +x %{name}
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Fri May 16 2025 Hector M <frieserpaldi@gmail.com> - 0.9.5-1
- Initial import
