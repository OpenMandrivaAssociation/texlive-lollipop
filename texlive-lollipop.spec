# revision 33676
# category Package
# catalog-ctan /macros/lollipop
# catalog-date 2014-04-19 12:16:09 +0200
# catalog-license gpl3
# catalog-version 1.03
Name:		texlive-lollipop
Version:	1.03
Release:	3
Summary:	TeX made easy
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/lollipop
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lollipop.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lollipop.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Provides:	texlive-lollipop.bin = %{EVRD}

%description
Lollipop is "TeX made easy" -- it is a macro package that
functions as a toolbox for writing TeX macros. Its main aim is
to make macro writing so easy that implementing a fully new
layout in TeX would become a matter of less than an hour for an
average document. The aim is that such a task could be
accomplished by someone with only a very basic training in TeX
programming. Thus, Lollipop aims to make structured text
formatting available in environments where typical users would
switch to WYSIWYG packages for the freedom that such a
mechanism offers. In addition, development of support for
Lollipop documents written in RTL languages (such as Persian)
is underway.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/lollipop
%{_bindir}/lualollipop
%{_bindir}/xelollipop
%{_texmfdistdir}/tex/lollipop/dvilollipop.ini
%{_texmfdistdir}/tex/lollipop/dvilualollipop.ini
%{_texmfdistdir}/tex/lollipop/lollipop-define.tex
%{_texmfdistdir}/tex/lollipop/lollipop-document.tex
%{_texmfdistdir}/tex/lollipop/lollipop-float.tex
%{_texmfdistdir}/tex/lollipop/lollipop-fontdefs.tex
%{_texmfdistdir}/tex/lollipop/lollipop-fonts.tex
%{_texmfdistdir}/tex/lollipop/lollipop-heading.tex
%{_texmfdistdir}/tex/lollipop/lollipop-lists.tex
%{_texmfdistdir}/tex/lollipop/lollipop-output.tex
%{_texmfdistdir}/tex/lollipop/lollipop-plain.tex
%{_texmfdistdir}/tex/lollipop/lollipop-text.tex
%{_texmfdistdir}/tex/lollipop/lollipop-tools.tex
%{_texmfdistdir}/tex/lollipop/lollipop.ini
%{_texmfdistdir}/tex/lollipop/lollipop.tex
%{_texmfdistdir}/tex/lollipop/lualollipop.ini
%{_texmfdistdir}/tex/lollipop/xelollipop.ini
%_texmf_fmtutil_d/lollipop
%doc %{_texmfdistdir}/doc/otherformats/lollipop/README
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/address.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/appendix.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/btxmac.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/comm.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/comment.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/example.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/extern.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/head.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/list.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/lollipop-manual.bib
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/lollipop-manual.pdf
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/lollipop-manual.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/mandefs.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/opt.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/out.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/prelim.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/struct.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/titlepag.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/manual/trace.tex
%doc %{_texmfdistdir}/doc/otherformats/lollipop/tex-inde.xen

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf pdftex lollipop
    ln -sf luatex lualollipop
    ln -sf xetex xelollipop
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/lollipop <<EOF
#
# from lollipop:
lollipop pdftex - -translate-file=cp227.tcx *lollipop.ini
lualollipop luatex - lualollipop.ini
xelollipop xetex - -etex xelollipop.ini
#! dvilollipop pdftex - -translate-file=cp227.tcx *lollipop.ini
#! dvilualollipop luatex - -translate-file=cp227.tcx lualollipop.ini
EOF
