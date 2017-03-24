Summary: NethServer alerts
Name: nethserver-alerts
Version: 0.1.0
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: nethserver-collectd
Requires: python-requests
Requires: collectd-python
Requires: python-daemon, python-setproctitle
BuildRequires: nethserver-devtools
BuildRequires: gettext
Obsoletes: ardad
Provides: ardad

%description
NethServer monitoring agent to trigger alarms

%post
/sbin/chkconfig --add nms
/sbin/service nms start

%preun
if [ $1 = 0 ]; then
        /sbin/service nms stop > /dev/null 2>&1
        /sbin/chkconfig --del nms
fi


%postun
if [ $1 -ge 1 ] ; then
        /sbin/service nms condrestart > /dev/null 2>&1 || :
fi



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
* Fri Mar 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.1.0-1
- Obsolete ardad - Nethesis/dev#5087
- Add "ardad --send" alias

* Mon Jan 23 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.9-1
- backup-alert: avoid duplicated and false alerts - Nethesis/dev#5050  Nethesis/dev#5049
- nsm: disable alerts on nslcd service - Nethesis/dev#5048

* Mon Nov 14 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.8-1
- backup-alert: avoid useless cron mails Nethesis/dev#5030

* Fri Oct 21 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.7-1
- added expand template and collectd restart on register-save. Nethesis/dev#5021
- lsm-update: avoid alerts on lsm restart.

* Mon Oct 10 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.6-1
- Fix backup status when backup does not exist.

* Thu Sep 22 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.5-1
- Fix backup alarm

* Fri Sep 09 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.4-1
- Change load threshold, add backup alert, improved LK handling - [NH:4209]

* Mon Jul 25 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.3-1
- First release of nms daemon [NH:4205]
- Hearbeats are now sent every 10 minutes

* Fri Jul 15 2016 Giovanni Bezicheri <giovanni.bezicheri@nethesis.it> - 0.0.2-1
- Refactor threshold.conf template and tuning of new alerts.

* Wed Jun 8 2016 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 0.0.1
- Initial release

