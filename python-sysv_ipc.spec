%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define oname sysv_ipc

Name:           python-%{oname}
Version:        0.4.2
Release:        1%{?dist}
Summary:        System V IPC for Python - Semaphores, Shared Memory and Message Queues
Group:          Development/Libraries
License:        GPLv3+
URL:            http://semanchuk.com/philip/%{oname}/
Source0:        http://semanchuk.com/philip/%{oname}/%{oname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  python-devel

%description
The sysv_ipc module which gives Python access to System V inter-process
semaphores, shared memory and message queues on systems that support them.

%package examples
Summary:    Examples for Python sysv_ipc module
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description examples
This module comes with two demonstration apps. The first (in the directory
demo) shows how to use shared memory and semaphores. The second (in the
directory demo2) shows how to use message queues.

%prep
%setup -q -n sysv_ipc-%{version}

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-examples-%{version}/demo{,2}
install -m 644 demo/*  $RPM_BUILD_ROOT/%{_docdir}/%{name}-examples-%{version}/demo
install -m 644 demo2/* $RPM_BUILD_ROOT/%{_docdir}/%{name}-examples-%{version}/demo2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc INSTALL LICENSE README ReadMe.html VERSION
%{python_sitearch}/%{oname}.so
%{python_sitearch}/%{oname}-%{version}-py2.6.egg-info

%files examples
%defattr(-,root,root,-)
%{_docdir}/%{name}-examples-%{version}/

%changelog
* Sat Aug 29 2009 Steven Fernandez <lonetwin@fedoraproject.org> - 0.4.2-1
- First build
