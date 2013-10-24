Summary:	Rerun is a structured approach to bash scripting
Name:		rerun
Version:	1.0.2
Release:	0.1
License:	Apache v2.0
Group:		Applications/System
Source0:	https://github.com/rerun/rerun/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ba2ee21993f680a7be3a6fe0891e7b1f
URL:		http://rerun.github.com/rerun
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_libdir		%{_prefix}/lib
%define	_libexecdir	%{_libdir}
%define	moddir		%{_libdir}/%{name}/modules/stubbs

%description
A simple command runner because it's easy to forget standard operating
procedure.

%prep
%setup -q

%build
%configure \
	--libdir=%{_prefix}/lib \
	--libexecdir=%{_prefix}/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT{%{moddir}/stubbs.1,%{_mandir}/man1}
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}

# package later
rm $RPM_BUILD_ROOT/etc/bash_completion.d/rerun


# TODO: remove after issue 147 fixed
#chmod 777 $RPM_BUILD_ROOT%{_prefix}/lib/rerun/modules $RPM_BUILD_ROOT%{moddir}/tests

%clean
rm -rf ${buildroot}

%files
%defattr(644,root,root,755)
%doc README README.md AUTHORS ChangeLog COPYING INSTALL NEWS
%attr(755,root,root) %{_bindir}/rerun
%{_mandir}/man1/stubbs.1*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/stubbs
%dir %{_libdir}/%{name}/tests
%{_libdir}/%{name}/tests/functions.sh
%attr(755,root,root) %{_libdir}/%{name}/tests/rerun-*.sh

%{moddir}/README.md
%{moddir}/metadata
%{moddir}/options
%{moddir}/templates

%dir %{moddir}/bin
%attr(755,root,root) %{moddir}/bin/Markdown.pl
%attr(755,root,root) %{moddir}/bin/roundup
%attr(755,root,root) %{moddir}/bin/shocco

%dir %{moddir}/lib
%{moddir}/lib/*.css
%attr(755,root,root) %{moddir}/lib/*.sh
%dir %{moddir}/lib/stub
%{moddir}/lib/stub/README.md
%dir %{moddir}/lib/stub/bash
%attr(755,root,root) %{moddir}/lib/stub/bash/generate-options
%{moddir}/lib/stub/bash/metadata
%dir %{moddir}/lib/stub/bash/templates
%{moddir}/lib/stub/bash/templates/functions.sh
%{moddir}/lib/stub/bash/templates/script

%dir %{moddir}/tests
%attr(755,root,root) %{moddir}/tests/*.sh

%dir %{moddir}/commands
%dir %{moddir}/commands/add-command
%{moddir}/commands/add-command/metadata
%{moddir}/commands/add-command/README.md
%attr(755,root,root) %{moddir}/commands/add-command/options.sh
%attr(755,root,root) %{moddir}/commands/add-command/script

%dir %{moddir}/commands/add-module
%{moddir}/commands/add-module/metadata
%{moddir}/commands/add-module/README.md
%attr(755,root,root) %{moddir}/commands/add-module/script

%dir %{moddir}/commands/add-option
%{moddir}/commands/add-option/metadata
%{moddir}/commands/add-option/README.md
%attr(755,root,root) %{moddir}/commands/add-option/script

%dir %{moddir}/commands/archive
%{moddir}/commands/archive/metadata
%{moddir}/commands/archive/README.md
%attr(755,root,root) %{moddir}/commands/archive/options.sh
%attr(755,root,root) %{moddir}/commands/archive/script

%dir %{moddir}/commands/docs
%{moddir}/commands/docs/metadata
%{moddir}/commands/docs/README.md
%attr(755,root,root) %{moddir}/commands/docs/options.sh
%attr(755,root,root) %{moddir}/commands/docs/script

%dir %{moddir}/commands/edit
%{moddir}/commands/edit/metadata
%{moddir}/commands/edit/README.md
%attr(755,root,root) %{moddir}/commands/edit/script

%dir %{moddir}/commands/migrate
%{moddir}/commands/migrate/metadata
%{moddir}/commands/migrate/README.md
%attr(755,root,root) %{moddir}/commands/migrate/options.sh
%attr(755,root,root) %{moddir}/commands/migrate/script

%dir %{moddir}/commands/rm-option
%{moddir}/commands/rm-option/metadata
%{moddir}/commands/rm-option/README.md
%attr(755,root,root) %{moddir}/commands/rm-option/script

%dir %{moddir}/commands/test
%{moddir}/commands/test/metadata
%{moddir}/commands/test/README.md
%attr(755,root,root) %{moddir}/commands/test/script
