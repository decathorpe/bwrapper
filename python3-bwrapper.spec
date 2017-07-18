%global srcname bwrapper

Name:           python3-%{srcname}
Summary:        Python wrapper around the bubblewrap CLI
Version:        0.1
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/decathorpe/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-psutil
BuildRequires:  python3-nose

Requires:       bubblewrap
Requires:       python3-nose
Requires:       python3-psutil

%{?python_provide:%python_provide python-%{srcname}}


%description
The "bwrapper" python3 module is a wrapper around the "bubblewrap" CLI.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files
%doc README.md
%license COPYING

%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue Jul 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Initial package.

