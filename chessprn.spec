Summary:	Utility to print chess games in various formats.
Name:		chessprn
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	ftp://chess.onenet.net/pub/chess/Unix/%{name}.tar.gz
# Source0-md5:	9f3fe9a548d319d2328fc0c98c521096
Source2:	Cheq.ps
Source3:	ftp://www.freechess.org/pub/chess/Unix/ChessFont.sh.gz
# Source3-md5:	8a694f8059c0270f2a57cdbca1e7ef8a
Patch0:		%{name}.diff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to print chess games in various formats.

%prep
%setup -q -n chessprn
%patch -p1
zcat ${RPM_SOURCE_DIR}/ChessFont.sh.gz | unshar
mv Font ChessFont.ps
mv README README.ChessFont

%build
%{__make}

%post
texhash

%postun
texhash

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_prefix}/lib/games/chessprn/tex}
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/chessprn
%{__make} LIBDIR=$RPM_BUILD_ROOT%{_prefix}/lib/games/chessprn \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} install
cp ${RPM_SOURCE_DIR}/Cheq.ps $RPM_BUILD_ROOT%{_prefix}/lib/games/chessprn
cp ChessFont.ps $RPM_BUILD_ROOT%{_prefix}/lib/games/chessprn/ChessFont.ps
cp -a $RPM_BUILD_ROOT%{_prefix}/lib/games/chessprn/tex/* \
	$RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/chessprn

%files
%defattr(644,root,root,755)
%doc notation.doc
%doc symboles.txt
%doc readme
%doc README.ChessFont Demo Table
%attr(755,root,root) /usr/bin/chessprn
/usr/lib/games/chessprn
/usr/share/texmf/tex/latex/chessprn
