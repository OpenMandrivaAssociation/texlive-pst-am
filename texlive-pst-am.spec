# revision 19591
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-am
# catalog-date 2010-09-04 14:00:25 +0200
# catalog-license lppl
# catalog-version 1.02
Name:		texlive-pst-am
Version:	1.02
Release:	2
Summary:	Simulation of modulation and demodulation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-am
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-am.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-am.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-am.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the simulation of the modulated and
demodulated amplitude of radio waves. The user may plot curves
of modulated signals, wave carrier, signal modulation, signal
recovery and signal demodulation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-am/pst-am.sty
%doc %{_texmfdistdir}/doc/generic/pst-am/Changes
%doc %{_texmfdistdir}/doc/generic/pst-am/README
%doc %{_texmfdistdir}/doc/generic/pst-am/index.phtml
%doc %{_texmfdistdir}/doc/generic/pst-am/pst-am-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-am/pst-am-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-am/pst-am-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-am/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
