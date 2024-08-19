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
install -d %{buildroot}/lib/systemd/system
install -d %{buildroot}/var/www/drefd-dash
install -d %{buildroot}/etc/httpd/conf.d
install -p -m 700 %{_builddir}/%{name}-%{version}/opt/drefd-dash/drefd_dash.sh %{buildroot}/opt/drefd-dash/drefd_dash.sh
install -p -m 700 %{_builddir}/%{name}-%{version}/opt/drefd-dash/drefd_dash.conf %{buildroot}/opt/drefd-dash/drefd_dash.conf
install -p -m 644 %{_builddir}/%{name}-%{version}/lib/systemd/system/drefd-dash.service %{buildroot}/lib/systemd/system/drefd-dash.service
cp -r %{_builddir}/%{name}-%{version}/var/www/drefd-dash/* %{buildroot}/var/www/drefd-dash/
install -p -m 644 %{_builddir}/%{name}-%{version}/etc/httpd/conf.d/drefd-dash.conf %{buildroot}/etc/httpd/conf.d/drefd-dash.conf

%files
%dir %attr(0700, root, root) /opt/drefd_dash/
%dir %attr(0755, apache, apache) /var/www/drefd-dash/
%attr(0700, root, root) /opt/drefd-dash/drefd_dash.sh
%attr(0700, root, root) /opt/drefd-dash/drefd_dash.conf
%attr(0644, root, root) /lib/systemd/system/drefd-dash.service
%attr(0644, root, root) /etc/httpd/conf.d/drefd-dash.conf

%post
chown -R apache:apache /var/www/drefd-dash
chmod -R 755 /var/www/drefd-dash
chcon -R -t httpd_sys_content_t /var/www/drefd-dash
systemctl daemon-reload
systemctl enable drefd-dash.service
systemctl start drefd-dash.service
systemctl restart httpd

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Sep 01 2024 Chris Andrist <github@utahdrn.org> - 1.0-0
- Initial Release
