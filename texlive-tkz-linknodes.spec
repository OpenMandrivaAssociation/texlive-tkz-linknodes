# revision 22833
# category Package
# catalog-ctan /macros/latex/contrib/tkz/tkz-linknodes
# catalog-date 2011-06-05 23:10:23 +0200
# catalog-license lppl
# catalog-version 1.0c
Name:		texlive-tkz-linknodes
Version:	1.0c
Release:	6
Summary:	Link nodes in mathematical environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-linknodes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-linknodes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-linknodes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package arose from a requirement to link the elements of an
amsmath align or aligned environment. The package makes use of
PGF/TikZ. The package documentation relies on the facilities of
the tkz-doc bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tkz-linknodes/tkz-linknodes.sty
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/README
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/examples/equation.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/examples/latex/equation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/examples/latex/quadratic.tex
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/examples/latex/system.tex
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/examples/quadratic.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/examples/system.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/latex/TKZdoc-linknodes-us.tex
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/latex/linknodes.ist
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/readme-linknodes.txt
%doc %{_texmfdistdir}/doc/latex/tkz-linknodes/tkz-linknodes-screen.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-2
+ Revision: 756996
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-1
+ Revision: 719767
- texlive-tkz-linknodes
- texlive-tkz-linknodes
- texlive-tkz-linknodes

