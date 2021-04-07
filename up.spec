# https://github.com/akavel/up
%global goipath         github.com/akavel/up
Version:                0.4

%gometa

%global common_description %{expand:
up is the Ultimate Plumber, a tool for writing Linux pipes in a terminal-based
UI interactively, with instant live preview of command results.}

%global golicenses    LICENSE

Name:           %{goname}
Release:        1%{?dist}
Summary:        Tools for testifying that your code will behave as you intend
License:        Apache 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/gdamore/tcell)
BuildRequires: golang(github.com/gdamore/tcell/terminfo)
BuildRequires: golang(github.com/mattn/go-isatty)
BuildRequires: golang(github.com/spf13/pflag)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/up %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license %{golicenses}
%{_bindir}/*

%gopkgfiles


%changelog
* Wed Apr 7 2021 Marek mr.Shu Šuppa <mr@shu.io> - 0.4
- First package for Fedora

