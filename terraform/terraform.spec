Name:          terraform
Version:       1.12.0
Release:       1%{?dist}
Summary:       Terraform enables you to safely and predictably create, change, and improve infrastructure.
Group:         Development Tools
URL:           https://www.terraform.io/
License:       MPL 2.0
Source0:       https://releases.hashicorp.com/terraform/%{version}/%{name}_%{version}_linux_amd64.zip
ExclusiveArch: x86_64

%define debug_package %{nil}

%description
Terraform enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Fri May 16 2025 Hector M <frieserpaldi@gmail.com> - 0.12.29-1
- Initial import
