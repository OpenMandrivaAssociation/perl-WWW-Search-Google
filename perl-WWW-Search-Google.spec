%define upstream_name    WWW-Search-Google
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Search Google via SOAP
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Net::Google)
BuildRequires:	perl(WWW::Search)
BuildArch:	noarch

%description
This class is a Google specialization of WWW::Search. It handles
searching Google http://www.google.com/ using its new SOAP API
http://www.google.com/apis/.

All interaction should be done through WWW::Search objects.

Note that you must register for a Google Web API account and have a
valid Google API license key before using this module.

This module reports errors via croak().

This module uses Net::Google to do all the dirty work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{perl_vendorlib}/WWW
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.0
+ Revision: 401892
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.23-2mdv2009.0
+ Revision: 268880
- rebuild early 2009.0 package (before pixel changes)

* Fri Apr 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2009.0
+ Revision: 195563
- spec cleanup
- update to new version 0.23

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.22-4mdv2008.0
+ Revision: 25465
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.22-3mdv2008.0
+ Revision: 23567
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.22-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.22-1mdk
- initial Mandriva package

