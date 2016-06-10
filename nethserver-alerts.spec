Summary: NethServer alerts
Name: nethserver-alerts
Version: 0.0.1
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: nethserver-collectd >= 1.2.0-1.4.g005fb6b.ns6
Requires: python-requests
Requires: collectd-python
BuildRequires: nethserver-devtools
BuildRequires: gettext

%description
NethServer monitoring agent to trigger alarms

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc LICENSE

%changelog
* Wed Jun 8 2016 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 0.0.1
- Initial release

