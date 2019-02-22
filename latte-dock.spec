#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : latte-dock
Version  : 0.8.6
Release  : 1
URL      : https://github.com/KDE/latte-dock/archive/v0.8.6.tar.gz
Source0  : https://github.com/KDE/latte-dock/archive/v0.8.6.tar.gz
Summary  : A dock based on Plasma Frameworks
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: latte-dock-bin = %{version}-%{release}
Requires: latte-dock-data = %{version}-%{release}
Requires: latte-dock-lib = %{version}-%{release}
Requires: latte-dock-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : kactivities-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : plasma-framework-dev
BuildRequires : qtbase-dev mesa-dev

%description
About
=====
Latte is a dock based on plasma frameworks that provides an elegant and intuitive experience for your tasks and plasmoids. It animates its contents by using parabolic zoom effect and trys to be there only when it is needed.

%package bin
Summary: bin components for the latte-dock package.
Group: Binaries
Requires: latte-dock-data = %{version}-%{release}
Requires: latte-dock-license = %{version}-%{release}

%description bin
bin components for the latte-dock package.


%package data
Summary: data components for the latte-dock package.
Group: Data

%description data
data components for the latte-dock package.


%package lib
Summary: lib components for the latte-dock package.
Group: Libraries
Requires: latte-dock-data = %{version}-%{release}
Requires: latte-dock-license = %{version}-%{release}

%description lib
lib components for the latte-dock package.


%package license
Summary: license components for the latte-dock package.
Group: Default

%description license
license components for the latte-dock package.


%prep
%setup -q -n latte-dock-0.8.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550846988
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1550846988
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/latte-dock
cp COPYING %{buildroot}/usr/share/package-licenses/latte-dock/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/latte-dock/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/latte-dock

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.latte-dock.desktop
/usr/share/dbus-1/interfaces/org.kde.LatteDock.xml
/usr/share/icons/breeze/applets/256/org.kde.latte.plasmoid.svg
/usr/share/icons/hicolor/16x16/apps/latte-dock.svg
/usr/share/icons/hicolor/22x22/apps/latte-dock.svg
/usr/share/icons/hicolor/24x24/apps/latte-dock.svg
/usr/share/icons/hicolor/32x32/apps/latte-dock.svg
/usr/share/icons/hicolor/48x48/apps/latte-dock.svg
/usr/share/icons/hicolor/scalable/apps/latte-dock.svg
/usr/share/knotifications5/lattedock.notifyrc
/usr/share/kservices5/kwin-script-activatelattelaunchermenu.desktop
/usr/share/kservices5/plasma-applet-audoban.applet.separator.desktop
/usr/share/kservices5/plasma-applet-org.kde.latte.containment.desktop
/usr/share/kservices5/plasma-applet-org.kde.latte.plasmoid.desktop
/usr/share/kservices5/plasma-applet-org.kde.latte.spacer.desktop
/usr/share/kservices5/plasma-containmentactions-lattecontextmenu.desktop
/usr/share/kservices5/plasma-shell-org.kde.latte.shell.desktop
/usr/share/kwin/scripts/activatelattelaunchermenu/contents/code/main.js
/usr/share/kwin/scripts/activatelattelaunchermenu/metadata.desktop
/usr/share/metainfo/audoban.applet.separator.appdata.xml
/usr/share/metainfo/org.kde.latte-dock.appdata.xml
/usr/share/metainfo/org.kde.latte.plasmoid.appdata.xml
/usr/share/metainfo/org.kde.latte.shell.appdata.xml
/usr/share/plasma/plasmoids/audoban.applet.separator/contents/ui/main.qml
/usr/share/plasma/plasmoids/audoban.applet.separator/metadata.desktop
/usr/share/plasma/plasmoids/audoban.applet.separator/metadata.json
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/code/AppletIdentifier.js
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/code/HeuristicTools.js
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/code/LayoutManager.js
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/code/MathTools.js
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/blueprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/brownprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/darkgreyprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/goldprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/greenprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/lightskyblueprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/orangeprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/pinkprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/purpleprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/redprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/icons/wheatprint.jpg
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/AddWidgetVisual.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/ColorizerManager.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/ConfigOverlay.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/DebugWindow.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/EditModeVisual.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/EditShadow.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/LayoutsContainer.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/PanelBox.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/ParabolicManager.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/Ruler.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/RulerMouseArea.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/VisibilityManager.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/ActiveIndicator.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/AppletHiddenSpacer.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/AppletItem.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/AppletItemWrapper.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/TitleTooltipParent.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.latte.containment/metadata.json
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/code/activitiesTools.js
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/code/layout.js
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/code/tools.js
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/images/panel-west.png
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/ContextMenu.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/MouseHandler.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/ParabolicManager.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/PulseAudio.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/ToolTipDelegate2.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/ToolTipInstance.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/ToolTipWindowMouseArea.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/config/ConfigAppearance.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/config/ConfigInteraction.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/config/ConfigPanel.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/AudioStream.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskActiveItem.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskDelegate.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskGroupItem.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskHiddenSpacer.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskIconItem.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskProgressOverlay.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskWindows.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskWrapper.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TitleTooltipParent.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/VisualAddItem.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/TaskClickedAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/TaskFastRestoreAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/TaskLauncherAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/TaskNewWindowAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/TaskRealRemovalAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/TaskRemoveWindowFromGroupAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/TaskRestoreAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/TaskShowWindowAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/metadata.json
/usr/share/plasma/plasmoids/org.kde.latte.spacer/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.latte.spacer/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.latte.spacer/contents/ui/ConfigAppearance.qml
/usr/share/plasma/plasmoids/org.kde.latte.spacer/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.latte.spacer/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.latte.spacer/metadata.json
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/AppearanceConfig.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/BehaviorConfig.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/Header.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/LatteCheckBoxStyle.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/LatteDockConfiguration.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/LatteDockSecondaryConfiguration.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/TasksConfig.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/TweaksConfig.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/TypeSelection.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/config.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/Slider.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/SpinBox.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/TextField.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/ToolTip.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/private/RoundShadow.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/defaults
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/splitter.svgz
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/trademark.svgz
/usr/share/plasma/shells/org.kde.latte.shell/contents/layouts/Default.latterc
/usr/share/plasma/shells/org.kde.latte.shell/contents/layouts/Extended.latterc
/usr/share/plasma/shells/org.kde.latte.shell/contents/layouts/Plasma.latterc
/usr/share/plasma/shells/org.kde.latte.shell/contents/layouts/Unity.latterc
/usr/share/plasma/shells/org.kde.latte.shell/contents/presets/Default.layout.latte
/usr/share/plasma/shells/org.kde.latte.shell/contents/presets/Extended.layout.latte
/usr/share/plasma/shells/org.kde.latte.shell/contents/presets/Plasma.layout.latte
/usr/share/plasma/shells/org.kde.latte.shell/contents/presets/Unity.layout.latte
/usr/share/plasma/shells/org.kde.latte.shell/contents/presets/multiple-layouts_hidden.layout.latte
/usr/share/plasma/shells/org.kde.latte.shell/contents/views/InfoView.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/views/Panel.qml
/usr/share/plasma/shells/org.kde.latte.shell/metadata.desktop
/usr/share/plasma/shells/org.kde.latte.shell/metadata.json
/usr/share/xdg/latte-layouts.knsrc

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/plasma_containmentactions_lattecontextmenu.so
/usr/lib64/qt5/qml/org/kde/latte/BadgeText.qml
/usr/lib64/qt5/qml/org/kde/latte/GlowPoint.qml
/usr/lib64/qt5/qml/org/kde/latte/liblattedockplugin.so
/usr/lib64/qt5/qml/org/kde/latte/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/latte-dock/COPYING
/usr/share/package-licenses/latte-dock/COPYING.LIB
