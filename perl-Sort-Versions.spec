#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	Versions
Summary:	Sort::Versions Perl module
Summary(cs):	Modul Sort::Versions pro Perl
Summary(da):	Perlmodul Sort::Versions
Summary(de):	Sort::Versions Perl Modul
Summary(es):	Módulo de Perl Sort::Versions
Summary(fr):	Module Perl Sort::Versions
Summary(it):	Modulo di Perl Sort::Versions
Summary(ja):	Sort::Versions Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Sort::Versions ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Sort::Versions
Summary(pl):	Modu³ perla Sort::Versions
Summary(pt_BR):	Módulo Perl Sort::Versions
Summary(pt):	Módulo de Perl Sort::Versions
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Sort::Versions
Summary(sv):	Sort::Versions Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Sort::Versions
Summary(zh_CN):	Sort::Versions Perl Ä£¿é
Name:		perl-Sort-Versions
Version:	1.5
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5434f948fdea6406851c77bebbd0ed19
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-SortVersions
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::Versions allows easy sorting of mixed non-numeric and numeric
strings, like the "version numbers" that many shared library systems
and revision control packages use.

%description -l pl
Modu³ Sort::Versions umo¿liwia ³atwe sortowanie ³añcuchów z³o¿onych z
przemieszanych znaków alfanumerycznych, takich jak numery wersji
bibliotek dzielonych lub numery rewizji u¿ywanych przez programy typu
RCS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Sort/Versions.pm
%{_mandir}/man3/*
