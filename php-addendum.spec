Summary:	DocBlock/JavaDoc annotations support for PHP 5
Name:		php-addendum
Version:	0.3.2
Release:	0.1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://addendum.googlecode.com/files/addendum-%{version}.zip
# Source0-md5:	cddbd1014e44b14f049fabaa5c7ecc4f
URL:		http://code.google.com/p/addendum/
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 4:5.0
Requires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{php_data_dir}/addendum

%description
DocBlock/JavaDoc annotations support for PHP5. Supporting single and
multi valued annotations accessible through extended Reflection API.

%prep
%setup -q -n addendum-%{version}
find -name '*.php' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/annotations
cp -a annotations.php $RPM_BUILD_ROOT%{_appdir}
cp -a annotations/*.php $RPM_BUILD_ROOT%{_appdir}/annotations

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
