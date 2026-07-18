%global tl_name xecjk
%global tl_revision 79660

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.10.2
Release:	%{tl_revision}.1
Summary:	Support for CJK documents in XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xecjk
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xecjk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xecjk.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xecjk.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ctex)
Requires:	texlive(fontspec)
Requires:	texlive(l3kernel)
Requires:	texlive(l3packages)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
xeCJK is a package for typesetting documents in Chinese, Japanese or
Korean with XeLaTeX. It provides CJK-specific automatic glue between CJK
and non-CJK characters, full control over CJK punctuation compression,
separate font families for CJK and Latin scripts, and a number of fine-
grained typographic refinements for the CJK script.

