%global debug_package %{nil}

Name:       lazygit
Version:    0.48.0
Release:    1%{?dist}
Summary:    Simple, pragmatic TUI (Terminal UI) frontend for GIT

License:    MIT
URL:        https://github.com/jesseduffield/lazygit
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: git-core >= 2.0
%if 0%{?fedora}
BuildRequires: go-md2man
%endif
BuildRequires: golang >= 1.18

%description
Simple, pragmatic TUI (Terminal UI) frontend for GIT. Written in Go with the 
gocui library.

From the official GIT repository:

Rant time: You've heard it before, git is powerful, but what good is that
power when everything is so damn hard to do? Interactive rebasing requires you
to edit a goddamn TODO file in your editor? Are you kidding me? To stage part
of a file you need to use a command line program to step through each hunk and
if a hunk can't be split down any further but contains code you don't want to
stage, you have to edit an arcane patch file by hand? Are you KIDDING me?!
Sometimes you get asked to stash your changes when switching branches only to
realise that after you switch and unstash that there weren't even any
conflicts and it would have been fine to just checkout the branch directly?
YOU HAVE GOT TO BE KIDDING ME!

If you're a mere mortal like me and you're tired of hearing how powerful git
is when in your daily life it's a powerful pain in your ass, lazygit might be
for you.


%prep
#----#

%autosetup -p1


%build
#-----#

go get
go build \
    -ldflags "-X main.version=%{version}" \
    -o _build/%{name}

%if 0%{?fedora}
  # Man page
  go-md2man -in README.md -out %{name}.1
%endif


%install
#-------#

install -Dpm 0755 _build/%{name} %{buildroot}%{_bindir}/%{name}

%if 0%{?fedora}
  # Man page
  install -Dpm 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
%endif


%files
#-----#

%license LICENSE
%doc README.md CONTRIBUTING.md docs/
%{_bindir}/%{name}
%if 0%{?fedora}
%{_mandir}/man1/*.1*
%endif


%changelog
