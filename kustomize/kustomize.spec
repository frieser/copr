%define debug_package %{nil}

Name:           kustomize
Version:        5.6.0
Release:        1%{?dist}
Summary:        Customization of kubernetes YAML configurations

License:        ASL 2.0
URL:            https://kustomize.io/
Source0:        https://github.com/kubernetes-sigs/%{name}/releases/download/%{name}%2Fv%{version}/%{name}_v%{version}_linux_amd64.tar.gz

%description
Kustomize introduces a template-free way to customize 
application configuration that simplifies the use of 
off-the-shelf applications. Now, built into kubectl as apply -k.

%prep
%autosetup -n %{name} -c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
