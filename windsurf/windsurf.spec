Name:           Windsurf
Version:        1.7.2
Release:        1%{?dist}
Summary:        Windsurf - The world's first agentic IDE

License:        Proprietary
URL:            https://codeium.com/windsurf
Source0:        https://windsurf-stable.codeiumdata.com/linux-x64/stable/619323b3cdd4a88a75f3b5fa39dba02c3b9e14a9/%{name}-linux-x64-%{version}.tar.gz
# Source0:        %{name}-%{version}.tar.gz

# Adjust these dependencies based on Windsurf's actual requirements
Requires:       gtk3 >= 3.24.0
Requires:       libnotify
Requires:       nss
Requires:       libXScrnSaver
Requires:       libXtst
Requires:       alsa-lib
Requires:       libxshmfence

%description
Windsurf is the world's first agentic IDE, powered by Cascade, a revolutionary AI coding assistant.
It enables developers to work both independently and collaboratively with AI to solve coding tasks efficiently.

%prep
%setup -q -n %{name}

%build
# No build process needed if distributing pre-built binaries
# Desactivar la generación de debuginfo para evitar errores de build-id
%global debug_package %{nil}    

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

# Find and copy icon file
find . -name "code.png" -exec cp {} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png \;

# Copy application files
cp -r * %{buildroot}%{_libdir}/%{name}/

# Create launcher script
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
exec %{_libdir}/%{name}/windsurf "$@"
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

# Desktop file
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Windsurf
Comment=The world's first agentic IDE
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;IDE;
StartupWMClass=Windsurf
EOF

%files
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
