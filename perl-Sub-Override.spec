%define upstream_name	 Sub-Override
%define upstream_version 0.09
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.09
Release:	3

Summary:	Perl extension for easily overriding subroutines
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/O/OV/OVID/Sub-Override-0.09.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildArch:	noarch

%description
Sub::Override is a perl module that allows the programmer to simply name a
subroutine to replace and to supply a sub to replace it with.

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
%doc Changes README
%{perl_vendorlib}/Sub/Override.pm
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 404422
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.08-6mdv2009.0
+ Revision: 258393
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.08-5mdv2009.0
+ Revision: 246479
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.08-3mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.08-3mdv2008.0
+ Revision: 23839
- rebuild


* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-2mdk
- Buildrequires fix

* Fri Sep 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.08-1mdk
- 0.08

* Tue Jan 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.06-1mdk
- Initial MDK release.


