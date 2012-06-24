%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	Versions
Summary:	Sort::Versions Perl module
Summary(pl):	Modu� Perla Sort::Versions
Name:		perl-Sort-Versions
Version:	1.4
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Obsoletes:	perl-SortVersions
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::Versions allows easy sorting of mixed non-numeric and numeric
strings, like the "version numbers" that many shared library systems
and revision control packages use.

%description -l pl
Modu� Sort::Versions umo�liwia �atwe sortowanie �a�cuch�w z�o�onych z
przemieszanych znak�w alfanumerycznych, takich jak numery wersji
bibliotek dzielonych lub numery rewizji u�ywanych przez programy typu
RCS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Sort/Versions.pm
%{_mandir}/man3/*
