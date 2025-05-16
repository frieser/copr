%define _build_id_links none
%global debug_package %{nil}

Name:          yq
Version:       4.45.1
Release:       1%{?dist}
Summary:       A portable command-line YAML, JSON, XML, CSV and properties processor

License:       MIT
URL:           https://github.com/mikefarah/yq/releases
Source0:       https://github.com/mikefarah/yq/releases/download/v%{version}/yq_linux_amd64.tar.gz
ExclusiveArch: x86_64

%description
a lightweight and portable command-line YAML, JSON and XML processor. yq uses
jq like syntax but works with yaml files as well as json, xml, properties, csv
and tsv. It does not yet support everything jq does - but it does support the
most common operations and functions, and more is being added continuously.

%prep
%autosetup -c

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1/
%{__install} -m 755 yq_linux_amd64 %{buildroot}/%{_bindir}/%{name}
%{__install} -m 644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
