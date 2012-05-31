%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-txaws
Version:        0.2.3
Release:        1%{?dist}
Summary:        Async library for EC2, OpenStack, and Eucalyptus

Group:          Applications/Internet
License:        MIT License
URL:            https://launchpad.net/txaws
Source0:        http://pypi.python.org/packages/source/t/txAWS/txAWS-%{version}.tar.gz

BuildArch:      noarch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  python python-devel
Requires:       python-dateutil
Requires:       python-twisted
Requires:       ca-certificates

%description
Twisted-based Asynchronous Libraries for Amazon Web Services and Eucalyptus
private clouds. This project's goal is to have a complete Twisted API
representing the spectrum of Amazon's web services as well as support for
Eucalyptus clouds.

%prep
%setup -q -n txAWS-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O2 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc README LICENSE
%{python_sitelib}/*
%{_bindir}/txaws-*
%{_bindir}/aws-status



%changelog
* Thu May 31 2012 Francisco Souza <f@souza.cc> - 0.2.3
- Initial packaging
