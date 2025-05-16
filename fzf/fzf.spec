%global debug_package %{nil}

Name:           fzf
Version:        0.62.0
Release:        1%{?dist}
Summary:        A command-line fuzzy finder

License:        MIT
URL:            https://github.com/junegunn/%{name}
Source:         https://github.com/junegunn/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git
BuildRequires:  go

%description
It's an interactive filter program for any kind of list; files,
command history, processes, hostnames, bookmarks, git commits, etc.
It implements a "fuzzy" matching algorithm, so you can quickly type in patterns
with omitted characters and still get the results you want.

%prep
%autosetup -n %{name}-%{version}

%build
go build -ldflags "-w -X main.version=%{version} \
                      -X main.revision=AllTheTools" \
                      -o %{name}

%install
install -Dpm 0755 %{name} -t %{buildroot}%{_bindir}/
install -Dpm 0755 bin/fzf-tmux -t %{buildroot}%{_bindir}/
install -Dpm 0644 man/man1/*.1 -t %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%doc README.md README-VIM.md CHANGELOG.md ADVANCED.md
%{_bindir}/%{name}
%{_bindir}/fzf-tmux
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/fzf-tmux.1*

%changelog
