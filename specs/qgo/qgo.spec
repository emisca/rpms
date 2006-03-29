# $Id$
# Authority: dries
# Upstream: Johannes Mesa Pascasio <frosla$sourceforge,net>

Summary: Go board, SGF editor and client for the Internet Go Server
Name: qgo
Version: 1.0.4
Release: 1
License: GPL
Group: Amusements/Games
URL: http://qgo.sourceforge.net/

Source: http://dl.sf.net/qgo/qgo-%{version}-r1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++

%description
qGo is a Go board, SGF editor, and client for the Internet Go Server. You can
review and edit games, connect to IGS, and play against a computer program
supporting GTP (like GnuGo). Go is an ancient board game which is very common
in Japan, China, and Korea.

%prep
%setup

%build
%configure
%{__ln_s} normaltools_gui.h src/normaltools.h
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/qgo
%{_datadir}/applnk/Games/qgo.desktop
%{_datadir}/mimelnk/text/sgf.desktop
%{_datadir}/qGo/

%changelog
* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1
- Initial package.
