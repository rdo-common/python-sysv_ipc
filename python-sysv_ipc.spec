%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define oname sysv_ipc

Name:           python-%{oname}
Version:        0.4.2
Release:        13%{?dist}
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
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
chmod -x demo*/*.{py,sh}
#sed -i -e '/^#!\//, 1d'  demo/mk.sh 



%files
%doc LICENSE README ReadMe.html VERSION
%{python_sitearch}/%{oname}.so
%{python_sitearch}/%{oname}-%{version}-py2.?.egg-info

%files examples
%doc demo/ demo2/

%changelog
* Sat Oct 10 2015 Athmane Madjoudj <athmane@fedoraproject.org> 0.4.2-13
- Use unversioned docdir  (RHBZ #994063)
- Fix some packaging issues

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.2-4
- further generalize the egginfo manifest so it works with any python 2 minor
version

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Sep 25 2009 Steven Fernandez <lonetwin@fedoraproject.org> - 0.4.2-2
- Spec file fix. Use correct python version for egg-info file

* Sat Aug 29 2009 Steven Fernandez <lonetwin@fedoraproject.org> - 0.4.2-1
- Initial build
