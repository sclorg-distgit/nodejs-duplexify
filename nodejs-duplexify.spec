%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name duplexify

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        3.4.2
Release:        3%{?dist}
Summary:        Turn a writeable and readable stream into a single streams2 duplex stream

License:        MIT
URL:            https://github.com/mafintosh/duplexify
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tape)
BuildRequires:  %{?scl_prefix}npm(tap)
BuildRequires:  %{?scl_prefix}npm(through2)
BuildRequires:  %{?scl_prefix}npm(concat-stream)
BuildRequires:  %{?scl_prefix}npm(end-of-stream)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%nodejs_fixdep end-of-stream ~1.x
%nodejs_fixdep readable-stream ~2.x

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
tap test.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 3.4.2-3
- Enable scl macros

* Fri Aug 14 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.4.2-1
- Update to 3.4.2

* Fri Aug 14 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.4.0-1
- Update to 3.4.0

* Wed Jul 22 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 3.2.0-3
- fixdep npm(readable-stream)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 3.2.0-1
- Initial packaging
