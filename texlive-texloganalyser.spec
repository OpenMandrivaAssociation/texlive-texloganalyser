# revision 19888
# category Package
# catalog-ctan /support/texloganalyser
# catalog-date 2010-07-22 14:36:43 +0200
# catalog-license other-free
# catalog-version 0.7
Name:		texlive-texloganalyser
Version:	0.7
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3

%description
The perl script allows the user to extract (and display)
elements of the log file.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texloganalyser
%{_texmfdistdir}/scripts/texloganalyser/texloganalyser
%doc %{_texmfdistdir}/doc/support/texloganalyser/README
%doc %{_tlpkgobjdir}/*.tlpobj

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
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
