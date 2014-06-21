# revision 34111
# category Package
# catalog-ctan /macros/xetex/latex/xecjk
# catalog-date 2014-05-17 22:15:48 +0200
# catalog-license lppl
# catalog-version 3.2.12
Name:		texlive-xecjk
Version:	3.2.12
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
have become used to, in the CJK package. The package requires a
current version of xtemplate (and hence of the current LaTeX 3
development environment).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xecjk/full-stop.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xecjk/full-stop.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xecjk/fullwidth-stop.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xecjk/fullwidth-stop.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xecjk/han-simp.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xecjk/han-simp.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xecjk/han-trad.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xecjk/han-trad.tec
%{_texmfdistdir}/tex/xelatex/xecjk/config/xeCJK.cfg
%{_texmfdistdir}/tex/xelatex/xecjk/xeCJK-listings.sty
%{_texmfdistdir}/tex/xelatex/xecjk/xeCJK.sty
%{_texmfdistdir}/tex/xelatex/xecjk/xeCJKfntef.sty
%{_texmfdistdir}/tex/xelatex/xecjk/xunicode-addon.sty
%{_texmfdistdir}/tex/xelatex/xecjk/xunicode-extra.def
%doc %{_texmfdistdir}/doc/xelatex/xecjk/README
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-CJKecglue.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-CJKfntef.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-IVS.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-autofake.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-checksingle.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-fallback.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-listings.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-punctstyle.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-subCJKblock.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xeCJK-example-verbatim.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xunicode-combine-marks.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xunicode-commands.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/example/xunicode-symbols.tex
%doc %{_texmfdistdir}/doc/xelatex/xecjk/xeCJK.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecjk/xunicode-symbols.pdf
#- source
%doc %{_texmfdistdir}/source/xelatex/xecjk/xeCJK.dtx
%doc %{_texmfdistdir}/source/xelatex/xecjk/xeCJK.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
