Name:               Photo
Summary:            A Zope product to manage images better
Version: 1.2.3
Release: %mkrel 9
Group:              Development/Python
Requires:           zope
License:            GPL
URL:                http://www.zope.org
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
