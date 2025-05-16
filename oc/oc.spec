# oc branch is being set here as a new default when both requirements are met:
# - It's at least oc-x.y.1 patch release in the x.y branch
# - OKD already has release in this branch

%global debug_package %{nil}
%global prjname oc
%global branch 4.18
# Change altprio to 0 if it's newest branch and still isn't considered as default here
# otherwise change it to the branch number without dots
%global altprio 418
# Change release_commit to the commit of current patch release in the branch
# oc doesn't have release tags, so we use the commit hash
# which is known from oc official release tarballs
%global release_commit eb9bc9b02fc27a48cceccc0140fc3f8ee1414c64

Name:           %{prjname}%{branch}
Version:        4.18.11
Release:        1%{?dist}
Summary:        The OpenShift Command Line, part of OKD. %{branch} branch

License:        Apache-2.0
URL:            https://github.com/openshift/%{prjname}
Source:         https://github.com/openshift/%{prjname}/archive/%{release_commit}.tar.gz

BuildRequires:  git-core
BuildRequires:  go
BuildRequires:  make
BuildRequires:  krb5-devel

Recommends:     %{name}-kubectl

%description
With OpenShift Client CLI (oc), you can create applications and manage OpenShift resources.
It is built on top of kubectl which means it provides its full capabilities
to connect with any kubernetes compliant cluster, and on top
adds commands simplifying interaction with an OpenShift cluster.

%package kubectl
Summary:        kubectl symlink to the OpenShift Command Line
Requires:       %{name} = %{version}-%{release}
Conflicts:      kubernetes-client
%description kubectl
Installs kubectl as a symlink to the OpenShift Client CLI (oc).

# Delete this package if %{branch} isn't considered as default
%package -n %{prjname}
Summary:        The OpenShift Command Line, part of OKD
Requires:       %{name} = %{version}-%{release}
Recommends:     %{prjname}-kubectl
%description -n %{prjname}
With OpenShift Client CLI (oc), you can create applications and manage OpenShift resources.
It is built on top of kubectl which means it provides its full capabilities
to connect with any kubernetes compliant cluster, and on top
adds commands simplifying interaction with an OpenShift cluster.

# Delete this package if %{branch} isn't considered as default
%package -n %{prjname}-kubectl
Summary:        kubectl symlink to the OpenShift Command Line
Requires:       %{prjname} = %{version}-%{release}
Requires:       %{name}-kubectl = %{version}-%{release}
Conflicts:      kubernetes-client
%description -n %{prjname}-kubectl
Installs kubectl as a symlink to the OpenShift Client CLI (oc).

%prep
%autosetup -n %{prjname}-%{release_commit}

%build
make oc SOURCE_GIT_COMMIT="%{release_commit}" SOURCE_GIT_TAG="v%{version}-AllTheTools"
offset=$(grep -obUaP --max-count=1 '\x00_RELEASE_VERSION_LOCATION_\x00XXX' "%{prjname}" | cut -d: -f1)
echo -n -e "%{version}\x00" | dd of="%{prjname}" bs=1 seek="$offset" conv=notrunc
ln -s %{prjname} kubectl

mkdir generated_completions
./%{prjname} completion bash > generated_completions/%{name}
./%{prjname} completion fish > generated_completions/%{name}.fish
./%{prjname} completion zsh  > generated_completions/_%{name}
./kubectl completion bash > generated_completions/kubectl%{branch}
./kubectl completion fish > generated_completions/kubectl%{branch}.fish
./kubectl completion zsh  > generated_completions/_kubectl%{branch}
# If it's not default branch:
# - Remove p; command from all sed commands below
# - Remove `%{prjname} `/`kubectl ` from replacement parts for zsh autocompletion
sed -i '/complete -o/{p;s/__start_oc %{prjname}/__start_oc %{name}/g;}' generated_completions/%{name}
sed -i '/complete -/{p;s/%{prjname} /%{name} /g;}'                      generated_completions/%{name}.fish
sed -i '/compdef/{s/ %{prjname}/ %{prjname} %{name}/g;}'                generated_completions/_%{name}
sed -i '/complete -o/{p;s/__start_kubectl kubectl/__start_kubectl kubectl%{branch}/g;}' generated_completions/kubectl%{branch}
sed -i '/complete -/{p;s/kubectl /kubectl%{branch} /g;}'                      generated_completions/kubectl%{branch}.fish
sed -i '/compdef/{s/ kubectl/ kubectl kubectl%{branch}/g;}'                   generated_completions/_kubectl%{branch}

%install
install -Dpm 0755 %{prjname} %{buildroot}%{_bindir}/%{name}
ln -s %{name} %{buildroot}%{_bindir}/kubectl%{branch}
install -Dpm 0644 generated_completions/%{name}      -t %{buildroot}/%{bash_completions_dir}/
install -Dpm 0644 generated_completions/%{name}.fish -t %{buildroot}/%{fish_completions_dir}/
install -Dpm 0644 generated_completions/_%{name}     -t %{buildroot}/%{zsh_completions_dir}/
install -Dpm 0644 generated_completions/kubectl%{branch}      -t %{buildroot}/%{bash_completions_dir}/
install -Dpm 0644 generated_completions/kubectl%{branch}.fish -t %{buildroot}/%{fish_completions_dir}/
install -Dpm 0644 generated_completions/_kubectl%{branch}     -t %{buildroot}/%{zsh_completions_dir}/

%post
alternatives --install %{_bindir}/%{prjname} %{prjname} %{_bindir}/%{name} %{altprio} \
    --follower %{bash_completions_dir}/%{prjname}      %{prjname}-bash-completion %{bash_completions_dir}/%{name} \
    --follower %{fish_completions_dir}/%{prjname}.fish %{prjname}-fish-completion %{fish_completions_dir}/%{name}.fish \
    --follower %{zsh_completions_dir}/_%{prjname}      %{prjname}-zsh-completion  %{zsh_completions_dir}/_%{name}

%post kubectl
alternatives --install %{_bindir}/kubectl kubectl %{_bindir}/kubectl%{branch} %{altprio} \
    --follower %{bash_completions_dir}/kubectl      %{prjname}-kubectl-bash-completion %{bash_completions_dir}/kubectl%{branch} \
    --follower %{fish_completions_dir}/kubectl.fish %{prjname}-kubectl-fish-completion %{fish_completions_dir}/kubectl%{branch}.fish \
    --follower %{zsh_completions_dir}/_kubectl      %{prjname}-kubectl-zsh-completion  %{zsh_completions_dir}/_kubectl%{branch}

%postun
if [ $1 -eq 0 ]; then
  alternatives --remove %{prjname} %{_bindir}/%{name}
fi

%postun kubectl
if [ $1 -eq 0 ]; then
  alternatives --remove kubectl %{_bindir}/kubectl%{branch}
fi

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%ghost %{_bindir}/%{prjname}
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}
%ghost %{bash_completions_dir}/%{prjname}
%ghost %{fish_completions_dir}/%{prjname}.fish
%ghost %{zsh_completions_dir}/_%{prjname}

%files kubectl
%license LICENSE
%doc README.md
%{_bindir}/kubectl%{branch}
%ghost %{_bindir}/kubectl
%{bash_completions_dir}/kubectl%{branch}
%{fish_completions_dir}/kubectl%{branch}.fish
%{zsh_completions_dir}/_kubectl%{branch}
%ghost %{bash_completions_dir}/kubectl
%ghost %{fish_completions_dir}/kubectl.fish
%ghost %{zsh_completions_dir}/_kubectl

# Delete this block if %{branch} isn't considered as default
%files -n %{prjname}
%license LICENSE
%doc README.md

# Delete this block if %{branch} isn't considered as default
%files -n %{prjname}-kubectl
%license LICENSE
%doc README.md

%changelog
