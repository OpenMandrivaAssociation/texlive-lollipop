Name:		texlive-lollipop
Version:	69742
Release:	1
Summary:	TeX made easy
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/lollipop
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lollipop.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lollipop.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/lollipop
%_texmf_fmtutil_d/lollipop
%doc %{_texmfdistdir}/doc/otherformats/lollipop

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

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
