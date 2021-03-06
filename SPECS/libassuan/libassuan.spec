Summary:	Provides IPC between GnuPG Components
Name:		libassuan
Version:	2.2.0
Release:	1
License:	GPLv3+
URL:		https://www.gnupg.org/(fr)/related_software/libassuan/index.html
Group:		General Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Requires:	libgpg-error >= 1.17
BuildRequires:	libgpg-error >= 1.17
%description
The libassuan package contains an inter process communication library used by some of the other GnuPG related packages. libassuan's primary use is to allow a client to interact with a non-persistent server. libassuan is not, however, limited to use with GnuPG servers and clients. It was designed to be flexible enough to meet the demands of many transaction based environments with non-persistent servers. 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_infodir}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files 
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*.h
%{_libdir}/*.so*
%{_datadir}/aclocal/*
%changelog
*	Tue Dec 30 2014 Divya Thaluru <dthaluru@vmware.com> 2.2.0-1
	Initial version
