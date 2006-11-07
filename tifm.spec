#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	smp		# don't build SMP module
%bcond_with	verbose		# verbose build (V=1)

%define		_rel	0.3
%define		_module	tifm
Summary:	Linux driver for TI FlashMedia xx12/xx21 storage controllers
Summary(pl):	Linuksowy sterownik dla kontrolerów pamiêci TI FlashMedia xx12/xx21
Name:		%{_module}
Version:	0.6b
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL v2
Group:		Base/Kernel
Source0:	http://download.berlios.de/tifmxx/%{name}-%{version}.tar.bz2
# Source0-md5:	e48d47260cda579362f14a9a81bd75dc
Patch0:		kernel-misc-%{name}-7420_7620.patch
URL:		http://developer.berlios.de/projects/tifmxx
%{?with_dist_kernel:BuildRequires:	kernel-module-build >= 3:2.6.7}
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

%description -l pl
Ten projekt s³u¿y rozwojowi akceptowalnego i maj±cego wolne ¼ród³a
linuksowego sterownika dla urz±dzeñ z rodziny TI FlashMedia.
Urz±dzenia te mo¿na znale¼æ w wiêkszo¶ci wspó³czesnych laptopów.
Niestety TI odmówi³ opublikowania pe³nej specyfikacji jakiegokolwiek z
urz±dzeñ FlashMedia czyni±c je bezu¿ytecznymi poza MS Windows (w
przeciwieñstwie do wielu innych producentów sprzêtu).

Sterowniki windowsowe dla wspomnianych urz±dzeñ s± dostêpne u prawie
ka¿dego du¿ego dostawcy komputerów dla platform Win32 i Win64.
Obs³uguj± ca³± oczekiwan± funkcjonalno¶æ: karty SM/xD, MMC, SD i SDIO,
MemoryStick i MSpro wraz z opcjami bezpieczeñstwa/DRM.

# kernel subpackages.
%package -n kernel-misc-%{_module}
Summary:	Linux driver for TI FlashMedia xx12/xx21 storage controllers
Summary(pl):	Sterownik dla Linuksa do kontrolerów pamiêci TI FlashMedia xx12/xx21
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%if %{with dist_kernel}
%requires_releq_kernel_up
Requires(postun):	%releq_kernel_up
%endif

%description -n kernel-misc-%{_module}
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

%description -n kernel-misc-%{_module} -l pl
Ten pakiet zawiera sterownik dla Linuksa do kontrolerów pamiêci TI
FlashMedia xx12/xx21.

Ten projekt s³u¿y rozwojowi akceptowalnego i maj±cego wolne ¼ród³a
linuksowego sterownika dla urz±dzeñ z rodziny TI FlashMedia.
Urz±dzenia te mo¿na znale¼æ w wiêkszo¶ci wspó³czesnych laptopów.
Niestety TI odmówi³ opublikowania pe³nej specyfikacji jakiegokolwiek z
urz±dzeñ FlashMedia czyni±c je bezu¿ytecznymi poza MS Windows (w
przeciwieñstwie do wielu innych producentów sprzêtu).

Sterowniki windowsowe dla wspomnianych urz±dzeñ s± dostêpne u prawie
ka¿dego du¿ego dostawcy komputerów dla platform Win32 i Win64.
Obs³uguj± ca³± oczekiwan± funkcjonalno¶æ: karty SM/xD, MMC, SD i SDIO,
MemoryStick i MSpro wraz z opcjami bezpieczeñstwa/DRM.

%package -n kernel-smp-misc-%{_module}
Summary:	Linux SMP driver for TI FlashMedia xx12/xx21 storage controllers
Summary(pl):	Sterownik dla Linuksa SMP do kontrolerów pamiêci TI FlashMedia xx12/xx21
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%if %{with dist_kernel}
%requires_releq_kernel_smp
Requires(postun):	%releq_kernel_smp
%endif

%description -n kernel-smp-misc-%{_module}
This package contains Linux SMP driver for TI FlashMedia xx12/xx21
storage controllers.

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

%description -n kernel-misc-%{_module} -l pl
Ten pakiet zawiera sterownik dla Linuksa SMP do kontrolerów pamiêci TI
FlashMedia xx12/xx21.

Ten projekt s³u¿y rozwojowi akceptowalnego i maj±cego wolne ¼ród³a
linuksowego sterownika dla urz±dzeñ z rodziny TI FlashMedia.
Urz±dzenia te mo¿na znale¼æ w wiêkszo¶ci wspó³czesnych laptopów.
Niestety TI odmówi³ opublikowania pe³nej specyfikacji jakiegokolwiek z
urz±dzeñ FlashMedia czyni±c je bezu¿ytecznymi poza MS Windows (w
przeciwieñstwie do wielu innych producentów sprzêtu).

Sterowniki windowsowe dla wspomnianych urz±dzeñ s± dostêpne u prawie
ka¿dego du¿ego dostawcy komputerów dla platform Win32 i Win64.
Obs³uguj± ca³± oczekiwan± funkcjonalno¶æ: karty SM/xD, MMC, SD i SDIO,
MemoryStick i MSpro wraz z opcjami bezpieczeñstwa/DRM.

%prep
%setup -q -c
%patch0 -p1

%build
# kernel module(s)
for cfg in %{?with_dist_kernel:%{?with_smp:smp} up}%{!?with_dist_kernel:nondist}; do
	if [ ! -r "%{_kernelsrcdir}/config-$cfg" ]; then
		exit 1
	fi
	install -d o/include/linux
	ln -sf %{_kernelsrcdir}/config-$cfg o/.config
	ln -sf %{_kernelsrcdir}/Module.symvers-$cfg o/Module.symvers
	ln -sf %{_kernelsrcdir}/include/linux/autoconf-$cfg.h o/include/linux/autoconf.h
%if %{with dist_kernel}
	%{__make} -j1 -C %{_kernelsrcdir} O=$PWD/o prepare scripts
%else
	install -d o/include/config
	touch o/include/config/MARKER
	ln -sf %{_kernelsrcdir}/scripts o/scripts
%endif
	%{__make} -C %{_kernelsrcdir} clean \
		RCS_FIND_IGNORE="-name '*.ko' -o" \
		M=$PWD O=$PWD/o KSRC=$PWD/o\
		%{?with_verbose:V=1}
	%{__make} -C %{_kernelsrcdir} modules \
		M=$PWD O=$PWD/o KSRC=$PWD/o\
		%{?with_verbose:V=1}
	for mod in tifm_7xx1 tifm_core tifm_sd; do
		mv $mod{,-$cfg}.ko
	done
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc

install %{_module}_7xx1-%{?with_dist_kernel:up}%{!?with_dist_kernel:nondist}.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/%{_module}_7xx1.ko
install %{_module}_core-%{?with_dist_kernel:up}%{!?with_dist_kernel:nondist}.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/%{_module}_core.ko
install %{_module}_sd-%{?with_dist_kernel:up}%{!?with_dist_kernel:nondist}.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/%{_module}_sd.ko
%if %{with smp} && %{with dist_kernel}
install %{_module}_7xx1-smp.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/%{_module}_7xx1.ko
install %{_module}_core-smp.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/%{_module}_core.ko
install %{_module}_sd-smp.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/%{_module}_sd.ko
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%post	-n kernel-smp-misc-%{_module}
%depmod %{_kernel_ver}smp

%postun -n kernel-smp-misc-%{_module}
%depmod %{_kernel_ver}smp

%files -n kernel-misc-%{_module}
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*

%if %{with smp} && %{with dist_kernel}
%files -n kernel-smp-misc-%{_module}
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*.ko*
%endif
