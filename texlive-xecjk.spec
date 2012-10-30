# revision 27996
# category Package
# catalog-ctan /macros/xetex/latex/xecjk
# catalog-date 2012-09-03 11:02:31 +0200
# catalog-license lppl
# catalog-version 3.0.8
Name:		texlive-xecjk
Version:	3.0.8
Release:	1
Summary:	Support for CJK documents in XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/xecjk
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecjk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecjk.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecjk.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for typesetting CJK documents in the way users
have become used to, in the CJK package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xecjk/xeCJK.sty
%doc %{_texmfdistdir}/doc/xelatex/xecjk/README
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-CJKecglue.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-autofake.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-checksingle.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-fallback.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-subCJKblock.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/xeCJK.pdf
#- source
%doc %{_texmfdistdir}/source/xelatex/xecjk/xeCJK.dtx
%doc %{_texmfdistdir}/source/xelatex/xecjk/xeCJK.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
