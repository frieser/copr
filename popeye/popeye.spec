%define debug_package %{nil}

Name:           popeye
Version:        0.22.1
Release:        0%{?dist}
Summary:        A Kubernetes cluster resource sanitizer

License:        ASL 2.0
URL:            https://popeyecli.io/
Source0:        https://github.com/derailed/popeye/releases/download/v%{version}/popeye_linux_amd64.tar.gz

%description
A Kubernetes cluster resource sanitizer

%prep
%autosetup -n %{name} -c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -p -m 755 %{name} %{buildroot}/usr/bin

%files
/usr/bin/popeye

%changelog
