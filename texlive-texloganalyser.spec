%global tl_name texloganalyser
%global tl_revision 54526
%global tl_bin_links texloganalyser:%{_texmfdistdir}/scripts/texloganalyser/texloganalyser

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11
Release:	%{tl_revision}.1
Summary:	Analyse TeX logs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texloganalyser
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texloganalyser.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texloganalyser.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texloganalyser.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This perl script allows the user to extract (and display) elements of
the log file.

