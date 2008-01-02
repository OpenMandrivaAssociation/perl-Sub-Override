%define module	Sub-Override
%define name	perl-%{module}
%define version	0.08
%define	release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension for easily overriding subroutines
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/O/OV/OVID/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl-Test-Exception

%description
Sub::Override is a perl module that allows the programmer to simply name a
subroutine to replace and to supply a sub to replace it with.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Sub/Override.pm
%{_mandir}/*/*

