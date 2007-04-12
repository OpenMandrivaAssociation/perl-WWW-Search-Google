%define real_name WWW-Search-Google

Summary:	WWW::Search::Google - Search Google via SOAP
Name:		perl-%{real_name}
Version:	0.22
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Net-Google >= 0.52
BuildRequires:	perl(WWW::Search)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/WWW/Search/Google.pm
%{_mandir}/*/*

