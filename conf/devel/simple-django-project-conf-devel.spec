%global _scl_prefix /opt/example_provider
%global pkg_base_name simple-django-project-conf-devel
%{?scl:%scl_package %{pkg_base_name}}
# required for bytecompiling settings.py
%{!?scl_python:%global scl_python python33}
%{!?scl_prefix_python:%global scl_prefix_python %{scl_python}-}

Name:           %{scl_prefix}%{pkg_base_name}
Version:        1
Release:        1%{?dist}
Summary:        Development configuration for simple-django-project
Group:          Development/Tools
License:        GPLv2
URL:            https://github.com/TomasTomecek/simple-django-project
Source0:        nginx-simple.conf
Source1:        settings.py
Source2:        uwsgi.ini
Source3:        uwsgi.service

BuildRequires:  %{?scl_prefix_python}python-devel
BuildRequires:  %{?scl_prefix_python}python-setuptools
BuildRequires:  sdp-build
BuildRequires:  sdp-runtime
BuildRequires:  systemd-units

BuildArch:      noarch

Provides:       simple-django-project-conf

%description
Development configuration for simple-django-project

%prep
rm -rf %{_builddir}/%{name}-%{version} || :
mkdir -p %{_builddir}/%{name}-%{version}
install %{sources} %{_builddir}/%{name}-%{version}

%install
cd %{_builddir}/%{name}-%{version}
install -p -D nginx-simple.conf %{buildroot}/%{_sysconfdir}/simple-django-project/nginx/nginx-simple.conf
install -p -D uwsgi.ini %{buildroot}/%{_sysconfdir}/simple-django-project/uwsgi/uwsgi.ini
install -p -D settings.py %{buildroot}%{python_sitelib}/simple/simple/settings.py
install -p -D uwsgi.service %{buildroot}%{_unitdir}/uwsgi.service

%files
%{_sysconfdir}/simple-django-project
%{python_sitelib}/simple/simple/
%{_unitdir}/uwsgi.service

%changelog
* Wed Aug 13 2014 Tomas Tomecek <ttomecek@redhat.com> - 1-1
- initial version
