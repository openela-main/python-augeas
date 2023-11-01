Name:		python-augeas
Version:	0.5.0
Release:	12%{?dist}
Summary:	Python bindings to augeas
Group:		Development/Languages
License:	LGPLv2+
URL:		http://augeas.net/
Source0:	http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.gz
Patch1:		0001-test-fix-discovery-of-location.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	python3-setuptools python3-devel
BuildRequires:	augeas python3-pytest

%description
python-augeas is a set of Python bindings around augeas.

%package -n python3-augeas
Summary:	Python 3 bindings to augeas
Requires:	augeas-libs
%{?python_provide:%python_provide python3-augeas}

%description -n python3-augeas
python3-augeas is a set of Python bindings around augeas.


%prep
%setup -q
%patch1 -p1

%{py3_build}
%{py3_install}

%check
pytest-3

%files -n python3-augeas
%license COPYING
%doc AUTHORS README.txt
%{python3_sitelib}/augeas.py
%{python3_sitelib}/python_augeas-*.egg-info
%{python3_sitelib}/__pycache__/*


%changelog
* Tue May 14 2019 Pino Toscano <ptoscano@redhat.com> - 0.5.0-12
- Run the tests during the build (RHBZ#1682268).

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.5.0-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 3 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5.0-5
- Modernize spec
- Fix python3 package file ownership

* Tue Jan 19 2016 Nils Philippsen <nils@redhat.com>
- use %%global instead of %%define

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 0.5.0-4
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 22 2014 Tomas Radej <tradej@redhat.com> - 0.5.0-2
- Added Python 3 subpackage

* Thu Sep 04 2014 Greg Swift <gregswift@gmail.com> - 0.5.0-1
- Version 0.5.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Greg Swift <gregswift@gmail.com> - 0.4.1-5
- add python-ctypes dependency (rhbz#1020239)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Greg Swift <gregswift@gmail.com> 0.4.1-1
- version 0.4.1
- include egg only on F-9, RHEL-6 and later

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 18 2011 Harald Hoyer <harald@redhat.com> 0.3.0-7
- only include egg-info, if fedora >=9 or rhel >= 6
Resolves: rhbz#661452

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3.0-2
- Rebuild for Python 2.6

* Tue Sep 09 2008 Harald Hoyer <harald@redhat.com> 0.3.0-1
- version 0.3.0

* Thu Jul 03 2008 Harald Hoyer <harald@redhat.com> 0.2.1-1
- version 0.2.1

* Wed Jun 11 2008 Harald Hoyer <harald@redhat.com> 0.2.0-1
- switched to noarch, dlopen/ python bindings

* Mon May 05 2008 Harald Hoyer <harald@redhat.com> 0.1.0-4
- version to import in CVS (rhbz#444945)

* Mon May 05 2008 Harald Hoyer <harald@redhat.com> 0.1.0-3
- set mode of _augeas.so to 0755

* Mon May 05 2008 Harald Hoyer <harald@redhat.com> 0.1.0-2
- wildcard to catch egg-info in case it is build

* Fri May 02 2008 Harald Hoyer <harald@redhat.com> 0.1.0-1
- new version

* Wed Apr 16 2008 Harald Hoyer <harald@redhat.com> - 0.0.8-1
- initial version
