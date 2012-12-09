# revision 27119
# category Package
# catalog-ctan /macros/xetex/latex/xecjk
# catalog-date 2012-07-20 19:39:58 +0200
# catalog-license lppl
# catalog-version 3.0.7
Name:		texlive-xecjk
Version:	3.0.7
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


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.0.7-1
+ Revision: 813182
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4.5-1
+ Revision: 772177
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4.4-2
+ Revision: 757587
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4.4-1
+ Revision: 719922
- texlive-xecjk
- texlive-xecjk
- texlive-xecjk

