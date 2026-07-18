%global tl_name lollipop
%global tl_revision 69742
%global tl_bin_links lollipop:tex

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.07
Release:	%{tl_revision}.1
Summary:	TeX made easy
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/formats/lollipop
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lollipop.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lollipop.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cm)
Requires:	texlive(hyphen-base)
Requires:	texlive(lollipop.bin)
Requires:	texlive(tex)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
Lollipop is "TeX made easy" -- it is a macro package that functions as a
toolbox for writing TeX macros. Its main aim is to make macro writing so
easy that implementing a fully new layout in TeX would become a matter
of less than an hour for an average document. The aim is that such a
task could be accomplished by someone with only a very basic training in
TeX programming. Thus, Lollipop aims to make structured text formatting
available in environments where typical users would switch to WYSIWYG
packages for the freedom that such a mechanism offers. In addition,
development of support for Lollipop documents written in RTL languages
(such as Persian) is underway.

