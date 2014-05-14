#
# Conditional build:
%bcond_with	tests	# make check (requires BES server)
#
Summary:	FreeForm data handler module for the OPeNDAP data server
Summary(pl.UTF-8):	Moduł obsługujący dane FreeForm dla serwera danych OPeNDAP
Name:		opendap-freeform_handler
Version:	3.8.8
Release:	1
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://www.opendap.org/pub/source/freeform_handler-%{version}.tar.gz
# Source0-md5:	f3d1518f5c462810be848eba73f6bf09
URL:		http://opendap.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
%{?with_tests:BuildRequires:	bes >= 3.13.0}
BuildRequires:	bes-devel >= 3.13.0
BuildRequires:	libdap-devel >= 3.13.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	bes >= 3.13.0
Requires:	libdap >= 3.13.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the FreeForm data handler module for the OPeNDAP data server.
It reads ASCII, binary and DB4 files which have been described using
FreeForm and returns DAP responses that are compatible with DAP2 and
the dap-server software.

%description -l pl.UTF-8
Ten pakiet zawiera moduł obsługujący dane FreeForm dla serwera danych
OPeNDAP. Odczytuje dane z plików ASCII, binarnych i DB4 opisane przy
użyciu FreeForm i zwraca odpowiedzi DAP zgodne z oprogramowaniem DAP2
i dap-server.

%prep
%setup -q -n freeform_handler-%{version}

%build
# rebuild autotools for -as-needed to work
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/bes/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/ff.conf
%attr(755,root,root) %{_libdir}/bes/libff_module.so
%dir %{_datadir}/hyrax/data/ff
%{_datadir}/hyrax/data/ff/*.dat
%{_datadir}/hyrax/data/ff/*.das
%{_datadir}/hyrax/data/ff/*.fmt
