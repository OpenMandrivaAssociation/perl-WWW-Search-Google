%define upstream_name    WWW-Search-Google
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Search Google via SOAP
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Net-Google >= 0.52
BuildRequires:	perl(WWW::Search)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/WWW
%{_mandir}/*/*
