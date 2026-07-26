%define upstream_name    Dist-Zilla-Plugin-UnusedVarsTests
Name:		perl-%{upstream_name}
Version:	1.100860
Release:	7

Summary:	Release tests for unused variables
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Dist-Zilla-Plugin-UnusedVarsTests
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Vars)
BuildArch:	noarch

%description
This is an extension of the Dist::Zilla::Plugin::InlineFiles manpage,
providing the following file:

  xt/release/unused-vars.t - a standard Test::Vars test

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*

