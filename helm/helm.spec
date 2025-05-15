%define debug_package %{nil}

Name:           helm
Version:        3.17.2
Release:        1%{?dist}
Summary:        The Kubernetes Package Manager
Group:          Applications/System
License:        ASL 2.0
URL:            https://helm.sh/
Source0:        https://get.helm.sh/%{name}-v%{version}-linux-amd64.tar.gz

%description
The Kubernetes Package Manager

%prep
%setup -qn linux-amd64

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
