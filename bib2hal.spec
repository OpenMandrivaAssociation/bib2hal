Name:       bib2hal
Version:    2.3
Release:    %mkrel 4
Summary:    Massive import BibTeX article into HAL
License:    GPL
Group:      Publishing
URL:        http://gforge.inria.fr/projects/bib2hal/
Source:     http://gforge.inria.fr/frs/download.php/4410/%{name}-%{version}.tar.gz
Patch0:     %{name}-2.3-fix-installation.patch
Patch1:     %{name}-2.3-create-man-page.patch
BuildRequires:  perl(Text::BibTeX)
BuildRequires:  perl(IO::Prompt)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(MIME::Base64)
BuildArch:  noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
bib2hal allows massive import BibTeX article into HAL.

%prep
%setup -q
%patch0 -p 1
%patch1 -p 1

%build
autoreconf
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog NEWS
%{_bindir}/%{name}.pl
%{_datadir}/%{name}
%{_mandir}/man1/bib2hal.pl.1*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3-4mdv2011.0
+ Revision: 616751
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 2.3-3mdv2010.0
+ Revision: 424617
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.3-2mdv2009.0
+ Revision: 266239
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.3-1mdv2009.0
+ Revision: 194629
- import bib2hal


* Thu Apr 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.3-1mdv2008.1
- first mdv release
