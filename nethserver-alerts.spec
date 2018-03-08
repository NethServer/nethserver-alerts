Summary: NethServer alerts
Name: nethserver-alerts
Version: 1.1.3
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: nethserver-collectd
Requires: python-requests
Requires: nethserver-lib >= 2.2.4-1
Requires: curl
Requires: nethserver-subscription
BuildRequires: nethserver-devtools
BuildRequires: gettext
BuildRequires: python2-devel

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
* Fri Sep 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.3-1
- Fix db permissions - Nethesis/dev#5180
- Fix table visualization

* Fri Jul 07 2017 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.2-1
- Check if alerts db is changed before overwriting it

* Tue Jun 27 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- Fix Italian translation

* Fri Jun 23 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- Customized alerts from my.nethesis.it - Nethesis/dev#5154

* Fri Apr 21 2017 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 1.0.6-1
Fix bad wan alert. Nethesis/dev#5100

* Mon Apr 10 2017 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 1.0.5-1
Fix RAID alert. Nethesis/dev#5099

* Fri Mar 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.4-1
- Add "ardad --send" alias - Nethesis/dev#5087

* Mon Jan 23 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1
- backup-alert: avoid duplicated and false alerts - Nethesis/dev#5050  Nethesis/dev#5049

* Mon Nov 14 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- backup-alert: avoid useless cron mails Nethesis/dev#5030

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

