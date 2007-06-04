#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_with	verbose		# verbose build (V=1)

%define		_rel	0.1
%define		_module	tifm
Summary:	Linux driver for TI FlashMedia xx12/xx21 storage controllers
Summary(pl.UTF-8):	Linuksowy sterownik dla kontrolerów pamięci TI FlashMedia xx12/xx21
Name:		%{_module}
Version:	0.8e
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL v2
Group:		Base/Kernel
Source0:	http://download.berlios.de/tifmxx/%{name}-%{version}.tar.bz2
# Source0-md5:	5a148e53eeaadde1d0e1284e367d563b
URL:		http://developer.berlios.de/projects/tifmxx
%{?with_dist_kernel:BuildRequires:	kernel-module-build >= 3:2.6.21}
BuildRequires:	rpmbuild(macros) >= 1.308
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is devoted to the development of the acceptable and free
source Linux driver for TI FlashMedia family of devices. These devices
are found in a vast majority of the modern laptops. Unfortunately, TI
refused to publish a complete datasheet for any of the FlashMedia
devices rendering them useless anywhere except MS Windows (not unlike
many other hardware vendors).

Windows drivers to the mentioned devices are available from nearly all
major computer vendors both for Win32 and Win64 platforms. They
support all the expected functionality: SM/xD cards, MMC, SD and SDIO,
MemoryStick and MSpro including security/DRM features.

%description -l pl.UTF-8
Ten projekt służy rozwojowi akceptowalnego i mającego wolne źródła
linuksowego sterownika dla urządzeń z rodziny TI FlashMedia.
Urządzenia te można znaleźć w większości współczesnych laptopów.
Niestety TI odmówił opublikowania pełnej specyfikacji jakiegokolwiek z
urządzeń FlashMedia czyniąc je bezużytecznymi poza MS Windows (w
przeciwieństwie do wielu innych producentów sprzętu).

Sterowniki windowsowe dla wspomnianych urządzeń są dostępne u prawie
każdego dużego dostawcy komputerów dla platform Win32 i Win64.
Obsługują całą oczekiwaną funkcjonalność: karty SM/xD, MMC, SD i SDIO,
MemoryStick i MSpro wraz z opcjami bezpieczeństwa/DRM.

# kernel subpackages.
%package -n kernel%{_alt_kernel}-misc-%{_module}
Summary:	Linux driver for TI FlashMedia xx12/xx21 storage controllers
Summary(pl.UTF-8):	Sterownik dla Linuksa do kontrolerów pamięci TI FlashMedia xx12/xx21
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-%{_module}
This package contains Linux driver for TI FlashMedia xx12/xx21 storage
controllers.

This project is devoted to the development of the acceptable and free
source Linux driver for TI FlashMedia family of devices. These devices
are found in a vast majority of the modern laptops. Unfortunately, TI
refused to publish a complete datasheet for any of the FlashMedia
devices rendering them useless anywhere except MS Windows (not unlike
many other hardware vendors).

Windows drivers to the mentioned devices are available from nearly all
major computer vendors both for Win32 and Win64 platforms. They
support all the expected functionality: SM/xD cards, MMC, SD and SDIO,
MemoryStick and MSpro including security/DRM features.

%description -n kernel%{_alt_kernel}-misc-%{_module} -l pl.UTF-8
Ten pakiet zawiera sterownik dla Linuksa do kontrolerów pamięci TI
FlashMedia xx12/xx21.

Ten projekt służy rozwojowi akceptowalnego i mającego wolne źródła
linuksowego sterownika dla urządzeń z rodziny TI FlashMedia.
Urządzenia te można znaleźć w większości współczesnych laptopów.
Niestety TI odmówił opublikowania pełnej specyfikacji jakiegokolwiek z
urządzeń FlashMedia czyniąc je bezużytecznymi poza MS Windows (w
przeciwieństwie do wielu innych producentów sprzętu).

Sterowniki windowsowe dla wspomnianych urządzeń są dostępne u prawie
każdego dużego dostawcy komputerów dla platform Win32 i Win64.
Obsługują całą oczekiwaną funkcjonalność: karty SM/xD, MMC, SD i SDIO,
MemoryStick i MSpro wraz z opcjami bezpieczeństwa/DRM.

%prep
%setup -q -c

%build
%build_kernel_modules -m %{_module}{_7xx1,_core,_sd}

%install
rm -rf $RPM_BUILD_ROOT
%install_kernel_modules  -s current -n %{_module} -m %{_module}{_7xx1,_core,_sd} -d misc

%clean
rm -rf $RPM_BUILD_ROOT

%post -n kernel%{_alt_kernel}-misc-%{_module}
%depmod %{_kernel_ver}

%postun -n kernel%{_alt_kernel}-misc-%{_module}
%depmod %{_kernel_ver}

%if %{with dist_kernel}
%files -n kernel%{_alt_kernel}-misc-%{_module}
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/%{_module}*.ko*
%{_sysconfdir}/modprobe.d/%{_kernel_ver}/%{name}.conf
%endif
