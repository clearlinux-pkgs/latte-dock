#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x55999050A2D9110E (mvourlakos@gmail.com)
#
Name     : latte-dock
Version  : 0.10.2
Release  : 20
URL      : https://download.kde.org/stable/latte-dock/latte-dock-0.10.2.tar.xz
Source0  : https://download.kde.org/stable/latte-dock/latte-dock-0.10.2.tar.xz
Source1  : https://download.kde.org/stable/latte-dock/latte-dock-0.10.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: latte-dock-bin = %{version}-%{release}
Requires: latte-dock-data = %{version}-%{release}
Requires: latte-dock-lib = %{version}-%{release}
Requires: latte-dock-license = %{version}-%{release}
Requires: latte-dock-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kactivities-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kirigami2-dev
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
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


%package locales
Summary: locales components for the latte-dock package.
Group: Default

%description locales
locales components for the latte-dock package.


%prep
%setup -q -n latte-dock-0.10.2
cd %{_builddir}/latte-dock-0.10.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634331081
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634331081
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/latte-dock
cp %{_builddir}/latte-dock-0.10.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/latte-dock/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/latte-dock-0.10.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/latte-dock/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/latte-dock-0.10.2/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/latte-dock/fa05e58320cb7c64786b26396f4b992579a628bc
cp %{_builddir}/latte-dock-0.10.2/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/latte-dock/49e61f7864169f2e356c11a17422d7d20d74b40f
cp %{_builddir}/latte-dock-0.10.2/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/latte-dock/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/latte-dock-0.10.2/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/latte-dock/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang latte-dock
%find_lang plasma_applet_org.kde.latte.containment
%find_lang plasma_applet_org.kde.latte.plasmoid
%find_lang plasma_containmentactions_lattecontextmenu
%find_lang latte_indicator_org.kde.latte.default
%find_lang latte_indicator_org.kde.latte.plasma

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
/usr/share/knsrcfiles/latte-indicators.knsrc
/usr/share/knsrcfiles/latte-layouts.knsrc
/usr/share/kservices5/plasma-containmentactions-lattecontextmenu.desktop
/usr/share/kservicetypes5/latte-indicator.desktop
/usr/share/latte/indicators/default/metadata.desktop
/usr/share/latte/indicators/default/package/config/config.qml
/usr/share/latte/indicators/default/package/config/main.xml
/usr/share/latte/indicators/default/package/ui/main.qml
/usr/share/latte/indicators/org.kde.latte.plasma/metadata.desktop
/usr/share/latte/indicators/org.kde.latte.plasma/package/config/config.qml
/usr/share/latte/indicators/org.kde.latte.plasma/package/config/main.xml
/usr/share/latte/indicators/org.kde.latte.plasma/package/ui/BackLayer.qml
/usr/share/latte/indicators/org.kde.latte.plasma/package/ui/FrontLayer.qml
/usr/share/latte/indicators/org.kde.latte.plasma/package/ui/main.qml
/usr/share/latte/indicators/org.kde.latte.plasmatabstyle/metadata.desktop
/usr/share/latte/indicators/org.kde.latte.plasmatabstyle/package/ui/BackLayer.qml
/usr/share/latte/indicators/org.kde.latte.plasmatabstyle/package/ui/main.qml
/usr/share/metainfo/org.kde.latte-dock.appdata.xml
/usr/share/metainfo/org.kde.latte.plasmoid.appdata.xml
/usr/share/metainfo/org.kde.latte.shell.appdata.xml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/code/AppletIdentifier.js
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/code/ColorizerTools.js
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/code/MathTools.js
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/BindingsExternal.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/DragDropArea.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/Upgrader.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/VisibilityManager.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/Animations.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/AutoSize.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/Debug.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/Indexer.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/Indicators.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/Launchers.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/Layouter.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/Metrics.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/MyView.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/ParabolicEffect.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/PositionShortcuts.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/ThinTooltip.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/UserRequests.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/AnimationsPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/IndexerPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/IndicatorsPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/LaunchersPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/LayouterPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/MetricsPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/MyViewPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/ParabolicEffectPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/PositionShortcutsPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/ThinTooltipPrivate.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/layouter/AppletsContainer.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/abilities/privates/metrics/Fraction.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/AppletItem.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/EventsSink.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/EventsSinkOriginArea.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/HiddenSpacer.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/IndicatorLevel.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/ItemWrapper.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/PaddingsInConfigureApplets.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/ParabolicArea.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/ShortcutBadge.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/TitleTooltipParent.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/colorizer/Applet.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/communicator/Actions.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/communicator/Engine.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/applet/communicator/LatteBridge.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/background/BackgroundProperties.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/background/MultiLayered.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/background/types/Paddings.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/background/types/Shadows.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/background/types/Totals.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/colorizer/CustomBackground.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/colorizer/KirigamiShadowedRectangle.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/colorizer/Manager.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/colorizer/NormalRectangle.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/debugger/DebugWindow.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/debugger/Tag.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/editmode/ConfigOverlay.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/layouts/AppletsContainer.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/layouts/EnvironmentActions.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/layouts/LayoutsContainer.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/layouts/loaders/Tasks.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.latte.containment/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.latte.containment/metadata.json
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/code/ColorizerTools.js
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/code/activitiesTools.js
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/code/layout.js
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/code/tools.js
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/images/panel-west.png
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/AppletAbilities.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/ContextMenu.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/PulseAudio.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/TasksExtendedManager.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/abilities/Launchers.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/abilities/launchers/Syncer.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/abilities/launchers/Validator.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/config/ConfigAppearance.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/config/ConfigInteraction.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/config/ConfigPanel.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/previews/PipeWireThumbnail.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/previews/PlasmaCoreThumbnail.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/previews/ToolTipDelegate2.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/previews/ToolTipInstance.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/previews/ToolTipWindowMouseArea.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/AudioStream.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/ProgressOverlay.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/SubWindows.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskIcon.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskItem.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/TaskMouseArea.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/ClickedAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/FastRestoreAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/LauncherAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/NewWindowAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/RealRemovalAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/RemoveWindowFromGroupAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/ShowWindowAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/launcher/BounceAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/task/animations/newwindow/BounceAnimation.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/taskslayout/MouseHandler.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/taskslayout/ScrollEdgeShadows.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/taskslayout/ScrollOpacityMask.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/taskslayout/ScrollPositioner.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/contents/ui/taskslayout/ScrollableList.qml
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.latte.plasmoid/metadata.json
/usr/share/plasma/shells/org.kde.latte.shell/contents/applet/CompactApplet.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/CanvasConfiguration.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/LatteDockConfiguration.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/LatteDockSecondaryConfiguration.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/canvas/HeaderSettings.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/canvas/SettingsOverlay.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/canvas/controls/Button.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/canvas/controls/GraphicIcon.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/canvas/controls/RearrangeIcon.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/canvas/controls/StickIcon.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/canvas/maxlength/Ruler.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/canvas/maxlength/RulerMouseArea.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/config.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/pages/AppearanceConfig.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/pages/BehaviorConfig.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/pages/EffectsConfig.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/configuration/pages/TasksConfig.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/CustomIndicatorButton.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/CustomVisibilityModeButton.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/DragCorner.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/IndicatorConfigUiManager.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/InnerShadow.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/controls/TypeSelection.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/defaults
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/blueprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/brownprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/darkgreyprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/defaultcustomprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/goldprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/greenprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/lightskyblueprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/orangeprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/pinkprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/purpleprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/redprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/canvas/wheatprint.jpg
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/splitter.svgz
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/trademark.svgz
/usr/share/plasma/shells/org.kde.latte.shell/contents/images/trademarkicon.svgz
/usr/share/plasma/shells/org.kde.latte.shell/contents/templates/.multiple-layouts_hidden.layout.latte
"/usr/share/plasma/shells/org.kde.latte.shell/contents/templates/Default Dock.view.latte"
"/usr/share/plasma/shells/org.kde.latte.shell/contents/templates/Default Panel.view.latte"
/usr/share/plasma/shells/org.kde.latte.shell/contents/templates/Default.layout.latte
"/usr/share/plasma/shells/org.kde.latte.shell/contents/templates/Empty Panel.view.latte"
/usr/share/plasma/shells/org.kde.latte.shell/contents/templates/Empty.layout.latte
/usr/share/plasma/shells/org.kde.latte.shell/contents/templates/Extended.layout.latte
/usr/share/plasma/shells/org.kde.latte.shell/contents/templates/Plasma.layout.latte
/usr/share/plasma/shells/org.kde.latte.shell/contents/templates/Unity.layout.latte
/usr/share/plasma/shells/org.kde.latte.shell/contents/views/AppletDelegate.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/views/InfoView.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/views/Panel.qml
/usr/share/plasma/shells/org.kde.latte.shell/contents/views/WidgetExplorer.qml
/usr/share/plasma/shells/org.kde.latte.shell/metadata.desktop
/usr/share/plasma/shells/org.kde.latte.shell/metadata.json

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kpackage/packagestructure/latte_packagestructure_indicator.so
/usr/lib64/qt5/plugins/plasma_containmentactions_lattecontextmenu.so
/usr/lib64/qt5/qml/org/kde/latte/abilities/bridge/Animations.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/bridge/BridgeItem.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/bridge/Indexer.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/bridge/Launchers.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/bridge/MyView.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/bridge/ParabolicEffect.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/bridge/PositionShortcuts.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/bridge/ThinTooltip.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/bridge/qmldir
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/Animations.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/AppletAbilities.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/Containment.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/Debug.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/Environment.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/Indexer.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/Indicators.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/Metrics.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/MyView.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/ParabolicEffect.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/PositionShortcuts.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/Requirements.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/ThinTooltip.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/UserRequests.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/appletabilities/ContainerAnchorBindings.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/appletabilities/ContainerGridBindings.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/appletabilities/ContainerListViewBindings.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/indicators/LatteConfiguration.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/indicators/LatteIndicator.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/client/qmldir
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/Animations.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/AppletRequirements.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/Containment.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/Debug.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/Environment.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/Indexer.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/Indicators.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/Metrics.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/MyView.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/ParabolicEffect.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/PositionShortcuts.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/ThinTooltip.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/UserRequests.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/animations/Duration.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/animations/Requirements.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/animations/SpeedFactor.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/animations/Tracker.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/indicators/IndicatorInfo.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/metrics/Margin.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/metrics/MarginsArea.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/metrics/Mask.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/metrics/Padding.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/metrics/Totals.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/metrics/mask/Thickness.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/myview/ItemShadow.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/paraboliceffect/Factor.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/paraboliceffect/PrivateProperties.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/definition/qmldir
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/Animations.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/Containment.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/Debug.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/Environment.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/Indicators.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/Metrics.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/MyView.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/ParabolicEffect.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/ThinTooltip.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/host/qmldir
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/BasicItem.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/IndicatorLevel.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/IndicatorObject.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/basicitem/HiddenSpacer.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/basicitem/IndicatorLevel.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/basicitem/ParabolicEventsArea.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/basicitem/ParabolicItem.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/basicitem/RestoreAnimation.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/basicitem/SeparatorItem.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/basicitem/ShortcutBadge.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/basicitem/TitleTooltipParent.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/indicators/LevelOptions.qml
/usr/lib64/qt5/qml/org/kde/latte/abilities/items/qmldir
/usr/lib64/qt5/qml/org/kde/latte/components/AddItem.qml
/usr/lib64/qt5/qml/org/kde/latte/components/AddingArea.qml
/usr/lib64/qt5/qml/org/kde/latte/components/BadgeText.qml
/usr/lib64/qt5/qml/org/kde/latte/components/CheckBox.qml
/usr/lib64/qt5/qml/org/kde/latte/components/CheckBoxesColumn.qml
/usr/lib64/qt5/qml/org/kde/latte/components/ComboBox.qml
/usr/lib64/qt5/qml/org/kde/latte/components/ComboBoxButton.qml
/usr/lib64/qt5/qml/org/kde/latte/components/ExternalShadow.qml
/usr/lib64/qt5/qml/org/kde/latte/components/GlowPoint.qml
/usr/lib64/qt5/qml/org/kde/latte/components/Header.qml
/usr/lib64/qt5/qml/org/kde/latte/components/HeaderSwitch.qml
/usr/lib64/qt5/qml/org/kde/latte/components/IndicatorItem.qml
/usr/lib64/qt5/qml/org/kde/latte/components/ItemDelegate.qml
/usr/lib64/qt5/qml/org/kde/latte/components/Label.qml
/usr/lib64/qt5/qml/org/kde/latte/components/ScrollArea.qml
/usr/lib64/qt5/qml/org/kde/latte/components/Slider.qml
/usr/lib64/qt5/qml/org/kde/latte/components/SpinBox.qml
/usr/lib64/qt5/qml/org/kde/latte/components/SpriteRectangle.qml
/usr/lib64/qt5/qml/org/kde/latte/components/SubHeader.qml
/usr/lib64/qt5/qml/org/kde/latte/components/Switch.qml
/usr/lib64/qt5/qml/org/kde/latte/components/TextField.qml
/usr/lib64/qt5/qml/org/kde/latte/components/ToolTip.qml
/usr/lib64/qt5/qml/org/kde/latte/components/code/ColorizerTools.js
/usr/lib64/qt5/qml/org/kde/latte/components/private/ButtonShadow.qml
/usr/lib64/qt5/qml/org/kde/latte/components/private/CheckBoxStyle.qml
/usr/lib64/qt5/qml/org/kde/latte/components/private/DefaultListItemBackground.qml
/usr/lib64/qt5/qml/org/kde/latte/components/private/MobileCursor.qml
/usr/lib64/qt5/qml/org/kde/latte/components/private/MobileTextActionsToolBar.qml
/usr/lib64/qt5/qml/org/kde/latte/components/private/RoundShadow.qml
/usr/lib64/qt5/qml/org/kde/latte/components/private/SwitchStyle.qml
/usr/lib64/qt5/qml/org/kde/latte/components/private/TextFieldFocus.qml
/usr/lib64/qt5/qml/org/kde/latte/components/qmldir
/usr/lib64/qt5/qml/org/kde/latte/core/liblattecoreplugin.so
/usr/lib64/qt5/qml/org/kde/latte/core/qmldir
/usr/lib64/qt5/qml/org/kde/latte/private/containment/liblattecontainmentplugin.so
/usr/lib64/qt5/qml/org/kde/latte/private/containment/qmldir
/usr/lib64/qt5/qml/org/kde/latte/private/tasks/liblattetasksplugin.so
/usr/lib64/qt5/qml/org/kde/latte/private/tasks/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/latte-dock/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/latte-dock/49e61f7864169f2e356c11a17422d7d20d74b40f
/usr/share/package-licenses/latte-dock/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/latte-dock/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/latte-dock/fa05e58320cb7c64786b26396f4b992579a628bc

%files locales -f latte-dock.lang -f plasma_applet_org.kde.latte.containment.lang -f plasma_applet_org.kde.latte.plasmoid.lang -f plasma_containmentactions_lattecontextmenu.lang -f latte_indicator_org.kde.latte.default.lang -f latte_indicator_org.kde.latte.plasma.lang
%defattr(-,root,root,-)

