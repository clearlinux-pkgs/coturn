#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : coturn
Version  : 4.5.1.1
Release  : 3
URL      : https://github.com/coturn/coturn/archive/4.5.1.1.tar.gz
Source0  : https://github.com/coturn/coturn/archive/4.5.1.1.tar.gz
Source1  : turnserver.service
Summary  : The TURN Server is a VoIP media traffic NAT traversal server and gateway
Group    : Development/Tools
License  : BSD-3-Clause OpenSSL
Requires: coturn-bin = %{version}-%{release}
Requires: coturn-data = %{version}-%{release}
Requires: coturn-license = %{version}-%{release}
Requires: coturn-man = %{version}-%{release}
Requires: coturn-services = %{version}-%{release}
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libevent)
Patch1: CVE-2020-6061.patch
Patch2: CVE-2020-6062.patch

%description
The TURN Server is a VoIP media traffic NAT traversal server and gateway. It
can be used as a general-purpose network traffic TURN server/gateway, too.

This implementation also includes some extra features. Supported RFCs:

TURN specs:
- RFC 5766 - base TURN specs
- RFC 6062 - TCP relaying TURN extension
- RFC 6156 - IPv6 extension for TURN
- Experimental DTLS support as client protocol.

STUN specs:
- RFC 3489 - "classic" STUN
- RFC 5389 - base "new" STUN specs
- RFC 5769 - test vectors for STUN protocol testing
- RFC 5780 - NAT behavior discovery support

The implementation fully supports the following client-to-TURN-server protocols:
- UDP (per RFC 5766)
- TCP (per RFC 5766 and RFC 6062)
- TLS (per RFC 5766 and RFC 6062); TLS1.0/TLS1.1/TLS1.2
- DTLS (experimental non-standard feature)

Supported relay protocols:
- UDP (per RFC 5766)
- TCP (per RFC 6062)

Supported user databases (for user repository, with passwords or keys, if
authentication is required):
- SQLite
- MySQL
- PostgreSQL
- Redis

Redis can also be used for status and statistics storage and notification.

Supported TURN authentication mechanisms:
- long-term
- TURN REST API (a modification of the long-term mechanism, for time-limited
  secret-based authentication, for WebRTC applications)

The load balancing can be implemented with the following tools (either one or a
combination of them):
- network load-balancer server
- DNS-based load balancing
- built-in ALTERNATE-SERVER mechanism.

%package bin
Summary: bin components for the coturn package.
Group: Binaries
Requires: coturn-data = %{version}-%{release}
Requires: coturn-license = %{version}-%{release}
Requires: coturn-services = %{version}-%{release}

%description bin
bin components for the coturn package.


%package data
Summary: data components for the coturn package.
Group: Data

%description data
data components for the coturn package.


%package dev
Summary: dev components for the coturn package.
Group: Development
Requires: coturn-bin = %{version}-%{release}
Requires: coturn-data = %{version}-%{release}
Provides: coturn-devel = %{version}-%{release}
Requires: coturn = %{version}-%{release}

%description dev
dev components for the coturn package.


%package doc
Summary: doc components for the coturn package.
Group: Documentation
Requires: coturn-man = %{version}-%{release}

%description doc
doc components for the coturn package.


%package license
Summary: license components for the coturn package.
Group: Default

%description license
license components for the coturn package.


%package man
Summary: man components for the coturn package.
Group: Default

%description man
man components for the coturn package.


%package services
Summary: services components for the coturn package.
Group: Systemd services

%description services
services components for the coturn package.


%prep
%setup -q -n coturn-4.5.1.1
cd %{_builddir}/coturn-4.5.1.1
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582667312
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
export SOURCE_DATE_EPOCH=1582667312
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/coturn
cp %{_builddir}/coturn-4.5.1.1/LICENSE %{buildroot}/usr/share/package-licenses/coturn/44edc3a7a30e912f10454aee90d312a5d0d7fa24
cp %{_builddir}/coturn-4.5.1.1/LICENSE.OpenSSL %{buildroot}/usr/share/package-licenses/coturn/c9c50bd46b69aba62e61c65d8ab08dd1e8c83b38
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/turnserver.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/turnadmin
/usr/bin/turnserver
/usr/bin/turnutils_natdiscovery
/usr/bin/turnutils_oauth
/usr/bin/turnutils_peer
/usr/bin/turnutils_stunclient
/usr/bin/turnutils_uclient

%files data
%defattr(-,root,root,-)
/usr/share/examples/turnserver/etc/turn_client_cert.pem
/usr/share/examples/turnserver/etc/turn_client_pkey.pem
/usr/share/examples/turnserver/etc/turn_server_cert.pem
/usr/share/examples/turnserver/etc/turn_server_pkey.pem
/usr/share/examples/turnserver/etc/turnserver.conf
/usr/share/examples/turnserver/scripts/basic/dos_attack.sh
/usr/share/examples/turnserver/scripts/basic/relay.sh
/usr/share/examples/turnserver/scripts/basic/tcp_client.sh
/usr/share/examples/turnserver/scripts/basic/tcp_client_c2c_tcp_relay.sh
/usr/share/examples/turnserver/scripts/basic/udp_c2c_client.sh
/usr/share/examples/turnserver/scripts/basic/udp_client.sh
/usr/share/examples/turnserver/scripts/loadbalance/master_relay.sh
/usr/share/examples/turnserver/scripts/loadbalance/slave_relay_1.sh
/usr/share/examples/turnserver/scripts/loadbalance/slave_relay_2.sh
/usr/share/examples/turnserver/scripts/loadbalance/tcp_c2c_tcp_relay.sh
/usr/share/examples/turnserver/scripts/loadbalance/udp_c2c.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_dos_attack.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_dtls_client.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_dtls_client_cert.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_relay.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_relay_cert.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_sctp_client.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_tcp_client.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_tcp_client_c2c_tcp_relay.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_tls_client.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_tls_client_c2c_tcp_relay.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_tls_client_cert.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_udp_c2c.sh
/usr/share/examples/turnserver/scripts/longtermsecure/secure_udp_client.sh
/usr/share/examples/turnserver/scripts/longtermsecuredb/secure_relay_with_db_mongo.sh
/usr/share/examples/turnserver/scripts/longtermsecuredb/secure_relay_with_db_mysql.sh
/usr/share/examples/turnserver/scripts/longtermsecuredb/secure_relay_with_db_mysql_ssl.sh
/usr/share/examples/turnserver/scripts/longtermsecuredb/secure_relay_with_db_psql.sh
/usr/share/examples/turnserver/scripts/longtermsecuredb/secure_relay_with_db_redis.sh
/usr/share/examples/turnserver/scripts/longtermsecuredb/secure_relay_with_db_sqlite.sh
/usr/share/examples/turnserver/scripts/mobile/mobile_dtls_client.sh
/usr/share/examples/turnserver/scripts/mobile/mobile_relay.sh
/usr/share/examples/turnserver/scripts/mobile/mobile_tcp_client.sh
/usr/share/examples/turnserver/scripts/mobile/mobile_tls_client_c2c_tcp_relay.sh
/usr/share/examples/turnserver/scripts/mobile/mobile_udp_client.sh
/usr/share/examples/turnserver/scripts/oauth.sh
/usr/share/examples/turnserver/scripts/pack.sh
/usr/share/examples/turnserver/scripts/peer.sh
/usr/share/examples/turnserver/scripts/readme.txt
/usr/share/examples/turnserver/scripts/restapi/secure_relay_secret.sh
/usr/share/examples/turnserver/scripts/restapi/secure_relay_secret_with_db_mongo.sh
/usr/share/examples/turnserver/scripts/restapi/secure_relay_secret_with_db_mysql.sh
/usr/share/examples/turnserver/scripts/restapi/secure_relay_secret_with_db_psql.sh
/usr/share/examples/turnserver/scripts/restapi/secure_relay_secret_with_db_redis.sh
/usr/share/examples/turnserver/scripts/restapi/secure_relay_secret_with_db_sqlite.sh
/usr/share/examples/turnserver/scripts/restapi/secure_udp_client_with_secret.sh
/usr/share/examples/turnserver/scripts/restapi/shared_secret_maintainer.pl
/usr/share/examples/turnserver/scripts/selfloadbalance/secure_dos_attack.sh
/usr/share/examples/turnserver/scripts/selfloadbalance/secure_relay.sh
/usr/share/schema.mongo.sh
/usr/share/schema.sql
/usr/share/schema.stats.redis
/usr/share/schema.userdb.redis
/usr/share/testmongosetup.sh
/usr/share/testredisdbsetup.sh
/usr/share/testsqldbsetup.sql

%files dev
%defattr(-,root,root,-)
/usr/include/turn/client/TurnMsgLib.h
/usr/include/turn/client/ns_turn_ioaddr.h
/usr/include/turn/client/ns_turn_msg.h
/usr/include/turn/client/ns_turn_msg_addr.h
/usr/include/turn/client/ns_turn_msg_defs.h
/usr/include/turn/client/ns_turn_msg_defs_experimental.h
/usr/include/turn/ns_turn_defs.h

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/turnserver/INSTALL
/usr/share/doc/turnserver/LICENSE
/usr/share/doc/turnserver/README.turnadmin
/usr/share/doc/turnserver/README.turnserver
/usr/share/doc/turnserver/README.turnutils
/usr/share/doc/turnserver/postinstall.txt
/usr/share/doc/turnserver/schema.mongo.sh
/usr/share/doc/turnserver/schema.sql
/usr/share/doc/turnserver/schema.stats.redis
/usr/share/doc/turnserver/schema.userdb.redis

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/coturn/44edc3a7a30e912f10454aee90d312a5d0d7fa24
/usr/share/package-licenses/coturn/c9c50bd46b69aba62e61c65d8ab08dd1e8c83b38

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man/man1/coturn.1
/usr/share/man/man/man1/turnadmin.1
/usr/share/man/man/man1/turnserver.1
/usr/share/man/man/man1/turnutils.1
/usr/share/man/man/man1/turnutils_natdiscovery.1
/usr/share/man/man/man1/turnutils_oauth.1
/usr/share/man/man/man1/turnutils_peer.1
/usr/share/man/man/man1/turnutils_stunclient.1
/usr/share/man/man/man1/turnutils_uclient.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/turnserver.service
