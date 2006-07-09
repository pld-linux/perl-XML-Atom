#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Atom
Summary:	perl(XML::Atom)
Summary(pl):	perl(XML::Atom)
Name:		perl-XML-Atom
Version:	0.19
Release:	0
# "same as perl" according to META.yml
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
#Patch0: %{name}
URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# most of CPAN modules have generic URL (substitute pdir and pnam here)
%if %{with autodeps} || %{with tests}
#BuildRequires:	perl-
#BuildRequires:	perl-
BuildRequires:	perl-DateTime
%endif
#Requires:	-
#Provides:	-
#Obsoletes:	-
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atom feed and API implementation.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# yes i know, its crude, but works, and its simple
perl -pi -e 's/^auto_install/#auto_install/' Makefile.PL;
#%patch0 -p1

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
# if module isn't noarch, use:
# %{__make} \
#	OPTIMIZE="%{rpmcflags}"

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
