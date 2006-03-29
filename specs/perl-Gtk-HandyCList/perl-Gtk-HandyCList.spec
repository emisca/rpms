# $Id$
# Authority: dag

%define real_name Gtk-HandyCList

Summary: Gtk-HandyCList module for perl
Name: perl-Gtk-HandyCList
Version: 0.031
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk-HandyCList/

Source: http://search.cpan.org/CPAN/authors/id/A/AR/ARISTOTLE/Gtk-HandyCList-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Gtk-HandyCList module for perl

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.031-1
- Updated to release 0.031.

* Sun Oct 12 2003 Dag Wieers <dag@wieers.com> - 0.02
- Initial package. (using DAR)
