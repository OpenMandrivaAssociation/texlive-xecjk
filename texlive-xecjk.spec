Name:		texlive-xecjk
Version:	3.6.0
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
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xecjk
%{_texmfdistdir}/tex/xelatex/xecjk
%doc %{_texmfdistdir}/doc/xelatex/xecjk
#- source
%doc %{_texmfdistdir}/source/xelatex/xecjk

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
