%global debug_package %{nil}
%undefine _package_note_file

Name: starship
Version:        1.22.1
Release: 1%{?dist}
Summary: Minimal, blazing-fast, and infinitely customizable prompt for any shell! â˜„ğŸŒŒï¸�

License: ISC
URL: https://github.com/starship/starship
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?el8} || 0%{?el9}
%else
BuildRequires: cargo >= 1.59
BuildRequires: rust >= 1.59
%endif
BuildRequires: cmake3
BuildRequires: gcc

BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(zlib)

%description
Minimal, blazing-fast, and infinitely customizable prompt for any shell! â˜„ğŸŒŒï¸�.


%prep
%autosetup
%if 0%{?el8} || 0%{?el9}
    curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
%endif


%install
export CARGO_PROFILE_RELEASE_BUILD_OVERRIDE_OPT_LEVEL=3
%if 0%{?el8} || 0%{?el9}
    $HOME/.cargo/bin/cargo install --root=%{buildroot}%{_prefix} --path=.
%else
    cargo install --root=%{buildroot}%{_prefix} --path=.
%endif
rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json
strip --strip-all %{buildroot}%{_bindir}/*


%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}


%changelog
