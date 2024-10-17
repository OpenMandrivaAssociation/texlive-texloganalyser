Name:		texlive-texloganalyser
Version:	54526
Release:	2
Summary:	Analyse TeX logs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texloganalyser
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texloganalyser.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texloganalyser.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/texloganalyser/texloganalyser texloganalyser
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
