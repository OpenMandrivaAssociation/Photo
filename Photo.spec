Name:               Photo
Summary:            A Zope product to manage images better
Version: 1.2.3
Release: %mkrel 9
Group:              Development/Python
Requires:           zope
License:            GPL
URL:                https://www.zope.org
BuildRoot:          %{_tmppath}/%{name}-%{version}-rootdir
Buildarch:	noarch

Source: %{name}-%{version}.tar.bz2

#----------------------------------------------------------------------
%description
This product provides a Photo object and a Photo Folder object for
managing digital images in Zope.  Photo objects provide multiple
configurable sizes of the photo.  Photo Folders provide a way to manage a
group of Photo objects by providing a way to specify display sizes and
properties for all contained photos.

#----------------------------------------------------------------------
%prep

rm -rf $RPM_BUILD_ROOT
%setup -a 0

#----------------------------------------------------------------------
%build

#----------------------------------------------------------------------
%install

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install %{name}-%{version}/*.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install %{name}-%{version}/*.txt $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/dtml
install %{name}-%{version}/dtml/*.dtml $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/dtml

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/Extensions
install %{name}-%{version}/Extensions/*.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/Extensions

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/help

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/www
install %{name}-%{version}/www/*.gif $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/www

%clean
rm -rf $RPM_BUILD_ROOT

#----------------------------------------------------------------------
%files
%defattr(-,root,root,0755)
%doc README.txt CHANGES.txt LICENSE.txt DEPENDENCIES.txt FAQ.txt THANKS.txt TODO.txt UPGRADE.txt version.txt

%{_libdir}/zope/lib/python/Products/%{name}/

#----------------------------------------------------------------------


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-9mdv2011.0
+ Revision: 616419
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2.3-8mdv2010.0
+ Revision: 430687
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.2.3-7mdv2009.0
+ Revision: 258966
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2.3-6mdv2009.0
+ Revision: 246861
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.2.3-4mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import Photo


* Fri May 13 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.2.3-4mdk
- Rebuild

* Wed Sep 05 2003 Sebastien Robin <seb@nexedi.com> 1.2.3-3mdk
- Update spec in order to follows Mandrake Rules

* Wed Apr 25 2003 Sebastien Robin <seb@nexedi.com> 1.2.3-2nxd
- Clean the spec file

* Mon Feb 3 2003 Jean-Paul Smets <jp@nexedi.com> 1.2.3-1nxd
- Initial release
