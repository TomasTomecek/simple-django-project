%global _scl_prefix /opt/example_provider

%global scl sdp
%scl_package %scl

%{!?scl_python:%global scl_python python33}
%{!?scl_prefix_python:%global scl_prefix_python %{scl_python}-}
%{!?__python3:%global __python3 %python33__python3}
# use scl python
%global __os_install_post %{%{scl_python}_os_install_post}
%global __python_requires %{%{scl_python}_python_requires}

# The directory for site packages for this Software Collection
%global _old_scl_prefix %(echo %{python33python_sitelib} | cut -d/ -f 1,2,3)
%global sdp_sitelib %(echo %{python33python_sitelib} | sed 's|%{scl_python}|%{scl}|' | sed 's|%{_old_scl_prefix}|%{_scl_prefix}|')


### METAPCKAGE ###
Summary: Package that installs %scl
Name: %scl_name
Version: 1
Release: 1%{?dist}
License: GPLv2
BuildRequires: scl-utils-build
BuildRequires: %{scl_prefix_python}scldevel
BuildRequires: %{scl_prefix_python}python-devel
BuildArch: noarch

%description
This is the main package for %scl Software Collection.


### RUNTIME ###
%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils
Requires: %{scl_prefix_python}runtime

%description runtime
Package shipping essential scripts to work with %scl Software Collection.


### BUILD ###
%package build
Summary: Package shipping basic build configuration
Requires: scl-utils-build
Requires: %{scl_prefix_python}scldevel

%description build
Package shipping essential configuration macros to build %scl Software Collection.

%prep
%setup -c -T

%install
%scl_install

cat >> %{buildroot}%{_scl_scripts}/enable << EOF
. scl_source enable %{scl_python}
export PYTHONPATH=%{sdp_sitelib}\${PYTHONPATH:+:\${PYTHONPATH}}
EOF

mkdir -p %{buildroot}%{sdp_sitelib}

cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl}-config << EOF
%%scl_package_override() %%{expand:%{?python33_os_install_post:%%global __os_install_post %%python33_os_install_post}
%%global __python_requires %%python33_python_requires
%%global __python_provides %%python33_python_provides
%%global __python %python33__python
%%global __python3 %python33__python
%%global python_sitelib %sdp_sitelib
%%global python3_sitelib %sdp_sitelib
}
EOF

%files

%files runtime
%scl_files
%sdp_sitelib

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%changelog
* Thu Aug 21 2014 Tomas Tomecek <ttomecek@redhat.com> - 1-1
- initial package

