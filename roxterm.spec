Summary:        A highly configurable terminal emulator
Name:           roxterm
Version:        3.12.1
Release:        1
License:        GPLv2+
Group:			Terminals
URL:            https://github.com/realh/roxterm
Source0:        https://github.com/realh/roxterm/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake ninja
BuildRequires:  docbook-style-xsl
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  xsltproc

%description
ROXTerm is a terminal emulator intended to provide similar features to
gnome-terminal, based on the same VTE library. It was originally designed
to have a smaller footprint and quicker start-up time by not using the
Gnome libraries and by using a separate applet to provide the configuration
GUI, but thanks to all the features it's acquired over the years ROXTerm
can probably now be accused of bloat. However, it is more configurable
than gnome-terminal and aimed more at "power" users who make heavy use
of terminals.

It still supports the ROX desktop application layout it was named after,
but can also be installed in a more conventional manner for use in other
desktop environments.

%files
%license COPYING
%doc AUTHORS README* docs
%{_bindir}/roxterm
%{_bindir}/roxterm-config
%{_datadir}/metainfo/roxterm.metainfo.xml
%{_datadir}/applications/roxterm.desktop
%{_datadir}/roxterm/
%{_datadir}/icons/hicolor/scalable/apps/roxterm.svg
%{_mandir}/man1/roxterm*.1*

#---------------------------------------------------------------------------

%prep
%autosetup

%build
%cmake \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

# fix docs
rm -fr %{buildroot}%{_docdir}/%{name}/{index.html,index.php,en,lib}

