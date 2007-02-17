%include	/usr/lib/rpm/macros.mono
Summary:	.NET language bindings for GtkSourceView
Summary(pl.UTF-8):	Wiązania GtkSourceView dla .NET
Name:		dotnet-gtksourceview-sharp2
Version:	0.10
Release:	5
License:	LGPL
Group:		Libraries
Source0:	http://go-mono.com/sources/gtksourceview-sharp-2.0/gtksourceview-sharp-2.0-%{version}.tar.gz
# Source0-md5:	2179634b8931e6be849a1e1f82c834e3
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	dotnet-gnome-sharp-devel >= 2.16.0
BuildRequires:	gtksourceview-devel >= 1.0.1
BuildRequires:	libtool
BuildRequires:	monodoc
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	pkgconfig
Requires:	dotnet-gnome-sharp >= 2.16.0
Requires:	mono >= 1.1.7
Requires:	gtksourceview >= 1.0.1
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides .NET bindings for GtkSourceView library.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania .NET do biblioteki GtkSourceView.

%package devel
Summary:	Development part of GtkSourceView#
Summary(pl.UTF-8):	Część GtkSourceView# przeznaczona dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gnome-sharp-devel >= 2.16.0

%description devel
Development part of GtkSourceView#.

%description devel -l pl.UTF-8
Część GtkSourceView# przeznaczona dla programistów.

%prep
%setup -q -n gtksourceview-sharp-2.0-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT`monodoc --get-sourcesdir`

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

# already in gtksourceview package
rm -f $RPM_BUILD_ROOT%{_datadir}/gtksourceview-1.0/language-specs/{csharp,nemerle,vbnet}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_prefix}/lib/mono/gac/*

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtksourceview-sharp-2.0
%{_datadir}/gapi-2.0/*
%{_pkgconfigdir}/*.pc
%{_libdir}/monodoc/sources/gtksourceview-sharp-*
