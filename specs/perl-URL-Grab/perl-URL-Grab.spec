# $Id$
# Authority: dag
# Upstream: Oliver Falk <oliver$linux-kernel,at>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URL-Grab

Summary: Perl module that drastically simplifies the fetching of files
Name: perl-URL-Grab
Version: 1.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URL-Grab/

Source: http://www.cpan.org/authors/id/O/OP/OPITZ/URL-Grab-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URL-Grab is a Perl module that drastically simplifies
the fetching of files.

This package contains the following Perl module:

    URL::Grab

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/URL::Grab.3pm*
%dir %{perl_vendorlib}/URL/
#%{perl_vendorlib}/URL/Grab/
%{perl_vendorlib}/URL/Grab.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)