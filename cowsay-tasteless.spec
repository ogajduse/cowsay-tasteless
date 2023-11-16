%global __requires_exclude .*Acme::Cow.*
%global cowsay cowsay
%global cowsdir %{_datadir}/%{cowsay}/cows

Name:           %{cowsay}-tasteless
Version:        3.7.0
Release:        1%{?dist}
Summary:        Tasteless .cow files for configurable speaking/thinking cow
License: GPL-2.0-or-later
URL:            https://github.com/cowsay-org/cowsay
Source0:        %{url}/archive/v%{version}/%{cowsay}-%{version}.tar.gz

BuildArch:      noarch
Requires:       %{cowsay} >= 3.7.0
Provides:       %{cowsay}-off = %{?epoch:%{epoch}:}%{version}-%{release}

%description
This package contains tasteless .cow files.

%prep
%setup -qn %{cowsay}-%{version}

%build
echo No need to build anything

%install
install -d -m 0755                                         $RPM_BUILD_ROOT%{cowsdir}
install -p -m 0644 share/cows/{bong,sodomized,satanic}.cow $RPM_BUILD_ROOT%{cowsdir}

# License issue
rm -f $RPM_BUILD_ROOT%{_datadir}/%{cowsay}/cows/daemon.cow

%files
%doc ChangeLog LICENSE.txt README*
%{cowsdir}/bong.cow
%{cowsdir}/sodomized.cow
%{cowsdir}/satanic.cow

%changelog
* Thu Nov 16 2023 Ondřej Gajdušek <ogajduse@redhat.com> 3.7.0-1
- Initial release

