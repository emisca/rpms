# $Id$

# Authority: dries
# Screenshot: http://qtparted.sourceforge.net/images/screenshot-001-a.jpg
# ScreenshotURL: http://qtparted.sourceforge.net/screenshots.en.html

# delayed: needs some other stuff packaged first
# NeedsCleanup

Summary: todo
Name: qtparted
Version: 0.4.1
Release: 1
License: GPL
Group: todo
URL: http://qtparted.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/qtparted/qtparted-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: progsreiserfs-devel


%description
todo

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)


%changelog
* Sun Dec 7 2003 Dries Verachtert <dries@ulyssis.org> 0.4.1-1
- first packaging for Fedora Core 1

