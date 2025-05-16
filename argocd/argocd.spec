%define _build_id_links none
%global debug_package %{nil}

Name:       	argocd
Version:    	2.14.9
Release:    	1%{?dist}
Summary:    	Declarative continuous deployment for Kubernetes

License:    	ASL 2.0
URL:        	https://github.com/argoproj/argo-cd/releases
Source0:    	https://github.com/argoproj/argo-cd/releases/download/v%{version}/argocd-linux-amd64
ExclusiveArch:	x86_64

%description
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
