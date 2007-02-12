Summary:	Utility to print chess games in various formats
Summary(pl.UTF-8):   Narzędzie do drukowania rozgrywek szachowych w różnych formatach
Name:		chessprn
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://kamp.pl/~havner/%{name}.tar.gz
# Source0-md5:	9f3fe9a548d319d2328fc0c98c521096
Source2:	Cheq.ps
Source3:	http://kamp.pl/~havner/ChessFont.sh.gz
# Source3-md5:	8a694f8059c0270f2a57cdbca1e7ef8a
Patch0:		%{name}.diff
BuildRequires:	flex
BuildRequires:	sharutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to print chess games in various formats.

%description -l pl.UTF-8
Narzędzie do drukowania rozgrywek szachowych w różnych formatach.

%prep
%setup -q -n chessprn
%patch0 -p1
zcat %{SOURCE3} | unshar
mv Font ChessFont.ps
mv README README.ChessFont

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_prefix}/lib/games/chessprn/tex}
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/chessprn

%{__make} install \
	LIBDIR=$RPM_BUILD_ROOT%{_prefix}/lib/games/chessprn \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_prefix}/lib/games/chessprn
cp ChessFont.ps $RPM_BUILD_ROOT%{_prefix}/lib/games/chessprn/ChessFont.ps
cp -a $RPM_BUILD_ROOT%{_prefix}/lib/games/chessprn/tex/* \
	$RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/chessprn

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/texhash
%postun	-p /usr/bin/texhash

%files
%defattr(644,root,root,755)
%doc notation.doc symboles.txt readme README.ChessFont Demo Table
%attr(755,root,root) %{_bindir}/chessprn
%{_prefix}/lib/games/chessprn
/usr/share/texmf/tex/latex/chessprn
