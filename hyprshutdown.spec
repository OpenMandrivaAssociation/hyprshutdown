Name:		hyprshutdown
Version:	0.1.0
Release:	1
Source0:	https://github.com/hyprwm/hyprshutdown/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	A graceful shutdown utility for Hyprland
URL:		https://github.com/hyprwm/hyprshutdown
License:	BSD-3-Clause
Group:		Window Manager/Hyprland
BuildRequires:	cmake
BuildRequires:  pkgconfig(hyprtoolkit)
BuildRequires:	pkgconfig(hyprutils) >= 0.11.0
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(libdrm)
BuildSystem:	cmake

%description
%summary.

%prep
%autosetup -p1

%files
%{_bindir}/%{name}
