# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mon

Summary: Mon module for perl
Name: perl-Mon
Version: 0.11
Release: 2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mon/

Source: http://www.cpan.org/modules/by-module/Mon/Mon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Mon module for perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING COPYRIGHT README VERSION
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Mon/

%changelog
* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 0.11-2
- Cosmetic cleanup.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
