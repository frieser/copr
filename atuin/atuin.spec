%global debug_package %{nil}

Name:    atuin
Version: 18.4.0
Release: 1%{?dist}
Summary: Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands.
Group:   Applications/System
License: MIT
Url:     https://atuin.sh     
Source0: https://github.com/atuinsh/%{name}/releases/download/v%{version}/%{name}-x86_64-unknown-linux-gnu.tar.gz

%description
Magical shell history.

%prep
%setup -qn %{name}-x86_64-unknown-linux-gnu

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
