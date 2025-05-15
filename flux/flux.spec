%define debug_package %{nil}

Name:           flux
Version:        2.5.1
Release:        1%{?dist}
Summary:        Open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit.

License:        Apache-2
URL:            https://fluxcd.io
Source0:        https://github.com/fluxcd/flux2/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz

%description
Flux is a tool for keeping Kubernetes clusters in sync 
with sources of configuration (like Git repositories and OCI artifacts), 
and automating updates to configuration when there is new code to deploy.

%prep
%autosetup -n %{name} -c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
