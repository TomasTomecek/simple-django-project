%global pkg_name simple-django-project
%{?scl:%scl_package %{pkg_name}}
%{!?scl_python:%global scl_python python33}
%{!?scl_prefix_python:%global scl_prefix_python %{scl_python}-}

Name:           %{scl_prefix}%{pkg_name}
Version:        1
Release:        1%{?dist}
Summary:        Simple django 1.7 project deployed on RHEL 7 with RHSCL
Group:          Development/Tools
License:        GPLv2
URL:            https://github.com/TomasTomecek/simple-django-project
Source0:        https://github.com/TomasTomecek/simple-django-project/releases/%{pkg_name}-%{version}.tar.gz

%{?scl:BuildRequires: %{scl}-build %{scl}-runtime}
%{?scl:Requires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix_python}python-devel
BuildRequires:  %{?scl_prefix_python}python-setuptools
BuildRequires:  sdp-build
BuildRequires:  sdp-runtime
Requires:       %{pkg_name}-conf
BuildArch:      noarch

%description
Simple django 1.7 project deployed on RHEL 7 with RHSCL

%prep
%setup -n %{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python3} setup.py build
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
%{__python3} setup.py install --skip-build --root %{buildroot} --install-purelib %{python_sitelib} --install-data %{python_sitelib}
%{?scl:"}
rm -f %{buildroot}%{python_sitelib}/simple/simple/settings.py*
rm -f %{buildroot}%{python_sitelib}/simple/simple/__pycache__/settings*

%files
%{python_sitelib}/simple/
%{python_sitelib}/simple_django_project-*.egg-info/
%attr(755, root, nginx) %{python_sitelib}/simple/manage.py

%changelog
* Wed Aug 13 2014 Tomas Tomecek <ttomecek@redhat.com> - 1-1
- initial version

