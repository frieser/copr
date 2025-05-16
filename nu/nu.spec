%global debug_package %{nil}

%define reponame nushell

Name:           nu
Version:        0.104.0
Release:        1%{?dist}
Summary:        A new type of shell

License:        MIT
URL:            https://github.com/nushell/%{reponame}
Source:         https://github.com/nushell/%{reponame}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  openssl-devel

%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif

%description
Nu takes cues from a lot of familiar territory: traditional shells like bash,
object based shells like PowerShell, gradually typed languages like TypeScript,
functional programming, systems programming, and more.
But rather than trying to be a jack of all trades, Nu focuses its energy on doing a few things well:
- Being a flexible cross-platform shell with a modern feel
- Solving problems as a modern programming language that works with the structure of your data
- Giving clear error messages and clean IDE support

%prep
%autosetup -n %{reponame}-%{version}

%build
cargo build --release --locked --workspace

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
