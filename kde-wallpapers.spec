Summary: KDE Wallpapers
Name:    kde-wallpapers
Version: 4.10.5
Release: 1%{?dist}

License: LGPLv3
URL:     http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-wallpapers-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: kdelibs4-devel >= %{version}
Requires: kde-filesystem

# Horos wallpaper moved back here in 4.6.1-2 (originally moved to main in 4.6.0-8)
Conflicts: kdebase-workspace < 4.6.1-2

# pkg renamed
Obsoletes: kdebase-workspace-wallpapers < 4.7.2-10
Provides:  kdebase-workspace-wallpapers = %{version}-%{release}

%description
%{summary}.


%prep
%setup -q 


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform} 


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files 
%doc LICENSE
%{_kde4_datadir}/wallpapers/Auros/
%{_kde4_datadir}/wallpapers/Ariya/
%{_kde4_datadir}/wallpapers/Autumn/
%{_kde4_datadir}/wallpapers/Azul/
%{_kde4_datadir}/wallpapers/Blue_Wood
%{_kde4_datadir}/wallpapers/Castilla_Sky/
%{_kde4_datadir}/wallpapers/Elarun/
%{_kde4_datadir}/wallpapers/Flores/
%{_kde4_datadir}/wallpapers/Flying_Field/
%{_kde4_datadir}/wallpapers/Fog_on_the_West_Lake/
%{_kde4_datadir}/wallpapers/Grass/
%{_kde4_datadir}/wallpapers/Hanami/
%{_kde4_datadir}/wallpapers/Horos/
%{_kde4_datadir}/wallpapers/Media_Life/
%{_kde4_datadir}/wallpapers/Prato/


%changelog
* Sun Jun 30 2013 Than Ngo <than@redhat.com> - 4.10.5-1
- 4.10.5

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Mon Apr 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.90-1
- 4.9.90

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Fri Jun 01 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.1-1
- 4.8.1

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.97-1
- 4.7.97

* Thu Dec 22 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95
- dropped wallpapers: Aghi, Evening, Fields_of_Peace, Quadros, Red_Leaf
- added wallpapers: Aryia, Azul, Castilla_Sky, Flying_Field, Fog_on_the_West_Lake

* Tue Dec 06 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.7.90-1
- 4.7.90

* Fri Nov 25 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.80-1
- 4.7.80

* Tue Nov 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-5
- 4.7.3

* Mon Oct 24 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-20
- kde-wallpapers first try

