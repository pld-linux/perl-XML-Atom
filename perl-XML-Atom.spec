#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"

%define		pdir	XML
%define		pnam	Atom
%include	/usr/lib/rpm/macros.perl
Summary:	XML::Atom - Atom feed and API implementation
Summary(pl.UTF-8):	XML::Atom - implementacja API Atom
Name:		perl-XML-Atom
Version:	0.41
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	99eeebbf90c95cc1a24426a0b9f2d6a5
URL:		http://search.cpan.org/dist/XML-Atom/
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-URI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} && %{with tests}
BuildRequires:	perl-DateTime
%endif
Requires:	perl-XML-XPath
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atom is a syndication, API, and archiving format for weblogs and other
data. XML::Atom implements the feed format as well as a client for the
API.

%description -l pl.UTF-8
Atom to API i format archiwów dla blogów i innych danych. XML::Atom
implementuje ten format, a także klienta dla tego API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# yes i know, its crude, but works, and its simple
%{__perl} -pi -e 's/^auto_install/#auto_install/' Makefile.PL;

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Atom.pm
%dir %{perl_vendorlib}/XML/Atom
%{perl_vendorlib}/XML/Atom/*.pm
%{_mandir}/man3/*
