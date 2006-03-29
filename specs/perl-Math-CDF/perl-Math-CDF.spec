# $Id$
# Authority: dries
# Upstream: Ed Callahan <cpan$edcallahan,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-CDF

Summary: Generate probabilities and quantiles from probability functions
Name: perl-Math-CDF
Version: 0.1
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-CDF/

Source: http://search.cpan.org/CPAN/authors/id/C/CA/CALLAHAN/Math-CDF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This package provides a perl interface to DCDFLIB, a set of C functions
written by Barry W. Brown, James Lovato and Kathy Russell of the
Department of Biomathematics at The University of Texas M.D. Anderson
Cancer Center in Houston, Texas. DCDFLIB code is included in this module
distribution with permission of its authors.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Math/CDF.pm
%{perl_vendorarch}/auto/Math/CDF

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
