%global debug_package %{nil}

Name:           zoxide
Version:        0.9.7
Release:        1%{?dist}
Summary:        A smarter cd command. Supports all major shells.

License:        MIT
URL:            https://github.com/ajeetdsouza/%{name}
Source:         https://github.com/ajeetdsouza/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust

Recommends:     fzf

%description
zoxide is a smarter cd command, inspired by z and autojump.

It remembers which directories you use most frequently,
so you can "jump" to them in just a few keystrokes.

zoxide works on all major shells.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/
install -Dpm 0644 man/man1/*.1 -t %{buildroot}/%{_mandir}/man1/

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/zoxide*.1*

%changelog
