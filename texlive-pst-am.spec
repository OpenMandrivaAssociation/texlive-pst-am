%global tl_name pst-am
%global tl_revision 19591

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	Simulation of modulation and demodulation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-am
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-am.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-am.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-am.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the simulation of the modulated and demodulated
amplitude of radio waves. The user may plot curves of modulated signals,
wave carrier, signal modulation, signal recovery and signal
demodulation.

