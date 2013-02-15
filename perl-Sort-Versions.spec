#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	Versions
Summary:	Sort::Versions Perl module - sorting of revision-like numbers
Summary(pl.UTF-8):	Moduł Perla Sort::Versions - sortowanie liczb typu numery rewizji
Name:		perl-Sort-Versions
Version:	1.5
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sort/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5434f948fdea6406851c77bebbd0ed19
URL:		http://search.cpan.org/dist/Sort-Versions/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-SortVersions
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::Versions allows easy sorting of mixed non-numeric and numeric
strings, like the "version numbers" that many shared library systems
and revision control packages use.

%description -l pl.UTF-8
Moduł Sort::Versions umożliwia łatwe sortowanie łańcuchów złożonych z
przemieszanych znaków alfanumerycznych, takich jak numery wersji
bibliotek dzielonych lub numery rewizji używanych przez programy typu
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
%{_mandir}/man3/Sort::Versions.3pm*
