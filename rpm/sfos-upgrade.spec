Name:          sfos-upgrade
Summary:       Scripts for safe and automated upgrading of SailfishOS with logging
Version:       0.9
Release:       1
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        %{name}-%{version}-%{release}.tar.gz
Source1:       https://github.com/Olf0/%{name}/archive/%{version}-%{release}.tar.gz
BuildArch:     noarch
Requires:      ssu
Requires:      sailfish-version
Requires:      curl

%description
%{summary}
Usage: sfos-upgrade [<version>]|[-h]|[--help]
With a version number provided as parameter it sets SSU to this version and in release mode before upgrading.  This is the regular use case.
Without a version number it extracts the one set for SSU to perform checks and balances, but does not alter SSU's settings before upgrading.

%prep
%setup -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp usr/bin/* %{buildroot}%{_bindir}/

%files
%defattr(0754,root,root,-)
%{_bindir}/%{name}
%{_bindir}/post_%{name}
%{_bindir}/tidy_log-dupes

