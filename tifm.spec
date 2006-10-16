#
# Replace MODULE_NAME with real module name and MODULE_DIR
# with required directory name.
#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_without	smp		# don't build SMP module
%bcond_without	userspace	# don't build userspace programs
%bcond_with	verbose		# verbose build (V=1)

%if %{without kernel}
%undefine	with_dist_kernel
%endif

#
# main package.
#
%define		_rel	0.1
Summary:	Free source linux driver for TI FlashMedia family of devices. 
Summary(pl):	Otwarty linuxowy sterownik dla urzadzen TI Flashmedia 
Name:		tifm
Version:	0.6b
Release:	%{_rel}
Epoch:		0
License:	GPL
Group:		kernel
# 
# Source0:	%{name}-%{version}.tar.gz
Source0:	http://download.berlios.de/tifmxx/%{name}-%{version}.tar.bz2
# Source0-md5:	e48d47260cda579362f14a9a81bd75dc
#Source1:	-
# Source1-md5:	-
#Patch0:	%{name}-what.patch
URL:		http://openfacts.berlios.de/index-en.phtml?title=TI_FlashMedia_xx12/xx21_driver
%if %{with kernel}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.14}
BuildRequires:	rpmbuild(macros) >= 1.308
%endif
#BuildRequires:	-
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free source linux driver for TI FlashMedia xx12/xx21 family of devices. 

%description -l pl
Otwarty linuxowy sterownik dla urzadzen TI Flasmedia xx12/xx21 

# kernel subpackages.

%package -n kernel%{_alt_kernel}-misc-tifm
Summary:	Linux driver for TI FlashMedia xx12/xx21 family of devices. 
Summary(pl):	Sterownik dla Linuksa do urzadzen TI FlashMedia xx12/xx21  
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%if %{with dist_kernel}
%requires_releq_kernel_up
Requires(postun):	%releq_kernel_up
%endif

%description -n kernel%{_alt_kernel}-misc-tifm
Driver for TI FlashMedia xx12/xx21 devices for Linux.

%description -n kernel%{_alt_kernel}-misc-tifm -l pl
Sterownik dla Linuksa do TI FlashMedia z rodziny xx12/xx21.

%package -n kernel%{_alt_kernel}-smp-misc-tifm
Summary:	Linux SMP driver for TI FlashMedia xx12/xx21
Summary(pl):	Sterownik dla Linuksa SMP do TI FlashMedia xx12/xx21
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%if %{with dist_kernel}
%requires_releq_kernel_smp
Requires(postun):	%releq_kernel_smp
%endif

%description -n kernel%{_alt_kernel}-smp-misc-tifm
This is driver for TI FlashMedia xx12/xx21 for Linux SMP.

%description -n kernel%{_alt_kernel}-smp-misc-tifm -l pl
Sterownik dla Linuksa SMP do urzadzen TI FlashMedia z serii xx12/xx21.

%prep

%build
%if %{with userspace}


%endif

%if %{with kernel}
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
#
#	patching/creating makefile(s) (optional)
#
	%{__make} -C %{_kernelsrcdir} clean \
		RCS_FIND_IGNORE="-name '*.ko' -o" \
		SYSSRC=%{_kernelsrcdir} \
		SYSOUT=$PWD/o \
		M=$PWD O=$PWD/o \
		%{?with_verbose:V=1}
	%{__make} -C %{_kernelsrcdir} modules \
		CC="%{__cc}" CPP="%{__cpp}" \
		SYSSRC=%{_kernelsrcdir} \
		SYSOUT=$PWD/o \
		M=$PWD O=$PWD/o \
		%{?with_verbose:V=1}

	mv tifm{,-$cfg}.ko
done
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}


%endif

%if %{with kernel}
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc
install tifm-%{?with_dist_kernel:up}%{!?with_dist_kernel:nondist}.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/tifm.ko
%if %{with smp} && %{with dist_kernel}
install tifm-smp.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/tifm.ko
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n kernel%{_alt_kernel}-misc-tifm
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-misc-tifm
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-smp-misc-tifm
%depmod %{_kernel_ver}smp

%postun	-n kernel%{_alt_kernel}-smp-misc-tifm
%depmod %{_kernel_ver}smp

%if %{with kernel}
%files -n kernel%{_alt_kernel}-misc-tifm
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*

%if %{with smp} && %{with dist_kernel}
%files -n kernel%{_alt_kernel}-smp-misc-tifm
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*.ko*
%endif
%endif

%if %{with userspace}
%files
%defattr(644,root,root,755)

%endif
