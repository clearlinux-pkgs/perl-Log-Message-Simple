#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Message-Simple
Version  : 0.10
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Log-Message-Simple-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Log-Message-Simple-0.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblog-message-simple-perl/liblog-message-simple-perl_0.10-3.debian.tar.xz
Summary  : 'Simplified interface to Log::Message'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Log-Message-Simple-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Log::Message)

%description
to Log::Message (a small and powerful generic message logging module)
Please type "perldoc Log::Message::Simple" after installation to see
the module usage information.

%package dev
Summary: dev components for the perl-Log-Message-Simple package.
Group: Development
Provides: perl-Log-Message-Simple-devel = %{version}-%{release}

%description dev
dev components for the perl-Log-Message-Simple package.


%package license
Summary: license components for the perl-Log-Message-Simple package.
Group: Default

%description license
license components for the perl-Log-Message-Simple package.


%prep
%setup -q -n Log-Message-Simple-0.10
cd ..
%setup -q -T -D -n Log-Message-Simple-0.10 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Log-Message-Simple-0.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Message-Simple
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Log-Message-Simple/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Log/Message/Simple.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Message::Simple.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Log-Message-Simple/deblicense_copyright
