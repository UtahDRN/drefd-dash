Name:           drefd-dash
Version:        1.0
Release:        1%{?dist}
Summary:        Simple Dashboard for DREFD Reflectors

License:        GPL
URL:            https://github.com/UtahDRN/drefd-dash
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Simple Dashboard for DREFD

%prep
%setup -q

%install
install -d %{buildroot}/opt/drefd-dash
install -d %{buildroot}/etc/cron.d
install -p -m 700 %{_builddir}/%{name}-%{version}/opt/drefd-dash/drefd_dash.sh %{buildroot}/opt/drefd-dash/drefd_dash.sh
install -p -m 700 %{_builddir}/%{name}-%{version}/opt/drefd-dash/drefd_dash.conf %{buildroot}/opt/drefd-dash/drefd_dash.conf
install -p -m 644 %{_builddir}/%{name}-%{version}/etc/cron.d/drefd_dash.cron %{buildroot}/etc/cron.d/drefd_dash.cron


%files
%dir %attr(0700, root, root) /opt/drefd_dash/
%attr(0700, root, root) /opt/drefd-dash/drefd_dash.sh
%attr(0700, root, root) /opt/drefd-dash/drefd_dash.conf
%attr(0644, root, root) /etc/cron.d/drefd_dash.cron

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Sep 01 2024 Chris Andrist <github@utahdrn.org> - 1.0-0
- Initial Release
