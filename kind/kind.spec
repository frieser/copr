%define _build_id_links none
%global debug_package %{nil}

Name:       kind
Version:    0.27.0
Release:    1%{?dist}
Summary:    Kubernetes IN Docker - local clusters for testing Kubernetes

License:    ASL 2.0
URL:        https://github.com/kubernetes-sigs/kind/releases
Source0:    https://github.com/kubernetes-sigs/kind/releases/download/v%{version}/%{name}-linux-amd64
Source1:    https://github.com/kubernetes-sigs/kind/releases/download/v%{version}/%{name}-linux-amd64.sha256sum
ExclusiveArch: x86_64

BuildRequires: coreutils

%description
kind is a tool for running local Kubernetes clusters using Docker container
"nodes". kind was primarily designed for testing Kubernetes itself, but may
be used for local development or CI.

%prep
pushd %{_sourcedir}
sha256sum --ignore-missing -c %{SOURCE1}
popd

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
