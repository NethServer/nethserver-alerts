Summary: NethServer alerts
Name: nethserver-alerts
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: nethserver-collectd
Requires: python-requests
BuildRequires: nethserver-devtools
BuildRequires: gettext

%description
NethServer monitoring agent to trigger alarms

%prep
%setup -q

%build
%{makedocs}
perl createlinks
mkdir -p root%{python2_sitelib}
mv -v nethserver_alerts.py root%{python2_sitelib}

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc LICENSE

%changelog
* Fri Oct 21 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Reconfigure collectd after server registration - Nethesis/dev#5021

* Thu Sep 22 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First NS7 release

* Fri Sep 09 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.4-1
- Change load threshold, add backup alert, improved LK handling - [NH:4209]

* Mon Jul 25 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.3-1
- First release of nms daemon [NH:4205]
- Hearbeats are now sent every 10 minutes

* Fri Jul 15 2016 Giovanni Bezicheri <giovanni.bezicheri@nethesis.it> - 0.0.2-1
- Refactor threshold.conf template and tuning of new alerts.

* Wed Jun 8 2016 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 0.0.1
- Initial release

