%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	Versions
Summary:	Sort::Versions Perl module
Summary(cs):	Modul Sort::Versions pro Perl
Summary(da):	Perlmodul Sort::Versions
Summary(de):	Sort::Versions Perl Modul
Summary(es):	M�dulo de Perl Sort::Versions
Summary(fr):	Module Perl Sort::Versions
Summary(it):	Modulo di Perl Sort::Versions
Summary(ja):	Sort::Versions Perl �⥸�塼��
Summary(ko):	Sort::Versions �� ����
Summary(no):	Perlmodul Sort::Versions
Summary(pl):	Modu� perla Sort::Versions
Summary(pt_BR):	M�dulo Perl Sort::Versions
Summary(pt):	M�dulo de Perl Sort::Versions
Summary(ru):	������ ��� Perl Sort::Versions
Summary(sv):	Sort::Versions Perlmodul
Summary(uk):	������ ��� Perl Sort::Versions
Summary(zh_CN):	Sort::Versions Perl ģ��
Name:		perl-Sort-Versions
Version:	1.4
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	58d447707fa9d252873dc34b70c507ee
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Sort/Versions.pm
%{_mandir}/man3/*