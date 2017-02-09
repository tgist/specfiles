Name:			simple-obfs
Version:		0.0.2
Release:		1%{?dist}
Summary:		A simple obfuscating tool

Group:			Applications/Internet
License:		GPLv3+
URL:			https://github.com/shadowsocks/%{name}
Source0:		%{url}/archive/v%{version}.tar.gz
AutoReq:		no
BuildRequires:	automake gcc libev-devel libsodium-devel make mbedtls-devel udns-devel xmlto zlib-devel xmlto
Requires:		libev libsodium udns pcre mbedtls


%description
Simple-obfs is a simple obfusacting tool, designed as plugin server of shadowsocks.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root)

%{_bindir}/*
%{_mandir}/man1/*
%{_docdir}/*


%changelog
