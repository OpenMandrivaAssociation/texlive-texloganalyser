# revision 26313
# category Package
# catalog-ctan /support/texloganalyser
# catalog-date 2010-07-22 14:36:43 +0200
# catalog-license other-free
# catalog-version 0.7
Name:		texlive-texloganalyser
Version:	0.7
Release:	5
Summary:	Analyse TeX logs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/texloganalyser
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texloganalyser.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texloganalyser.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texloganalyser.bin = %{EVRD}

%description
The perl script allows the user to extract (and display)
elements of the log file.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texloganalyser
%{_texmfdistdir}/scripts/texloganalyser/texloganalyser
%doc %{_texmfdistdir}/doc/support/texloganalyser/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texloganalyser/texloganalyser texloganalyser
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7-3
+ Revision: 812911
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7-2
+ Revision: 756740
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7-1
+ Revision: 719705
- texlive-texloganalyser
- texlive-texloganalyser
- texlive-texloganalyser

