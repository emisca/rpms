# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-TrulyRandom

Summary: Perl interface to a truly random number generator function
Name: perl-Math-TrulyRandom
Version: 1.0
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-TrulyRandom/

Source: http://www.cpan.org/modules/by-module/Math/Math-TrulyRandom-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl interface to a truly random number generator function.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Change to real perl. (Please fix upstream)
%{__perl} -pi -e 's|^#!\s+/.*bin/perl|#!%{__perl}|i' *.pm

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/*
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/TrulyRandom.pm
%dir %{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/auto/Math/TrulyRandom/

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
