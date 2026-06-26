import QtQuick
import QtQuick.Controls as QQC2
import QtQuick.Layouts
import org.kde.kirigami as Kirigami

import ".." as Widget
import "../libconfig" as LibConfig


LibConfig.FormKCM {
	id: page

	property alias cfg_ctrl_click_command: ctrl_click_command.text
	property alias cfg_middle_click_command: middle_click_command.text
	property alias cfg_shift_click_command: shift_click_command.text
	property alias cfg_alt_click_command: alt_click_command.text
	property alias cfg_ctrl_mousewheel_up: ctrl_mousewheel_up.text
	property alias cfg_ctrl_mousewheel_down: ctrl_mousewheel_down.text

	property int indentWidth: 24 * Screen.devicePixelRatio

	//-------------------------------------------------------
	LibConfig.Heading {
		text: i18n("Advanced Click Actions")
		useThickTopMargin: false
		label.Layout.topMargin: 0
	}

	LibConfig.CommandFieldWithPresets {
		Kirigami.FormData.label: i18n("Ctrl+Click Command:")
		id: ctrl_click_command
	}

	LibConfig.CommandFieldWithPresets {
		Kirigami.FormData.label: i18n("Middle Click Command:")
		id: middle_click_command
	}

	LibConfig.CommandFieldWithPresets {
		Kirigami.FormData.label: i18n("Shift+Click Command:")
		id: shift_click_command
	}

	LibConfig.CommandFieldWithPresets {
		Kirigami.FormData.label: i18n("Alt+Click Command:")
		id: alt_click_command
	}

	//-------------------------------------------------------
	LibConfig.Heading {
		text: i18n("Advanced Mouse Wheel Actions")
	}

	LibConfig.SpinBox {
		Kirigami.FormData.label: i18n("Ctrl+Scroll Cooldown:")
		configKey: 'ctrl_mousewheel_cooldown'
		suffix: i18n("ms")
		stepSize: 100
		from: 0
		to: 5000
	}

	LibConfig.CommandFieldWithPresets {
		Kirigami.FormData.label: i18n("Ctrl+Scroll Up:")
		id: ctrl_mousewheel_up
	}

	LibConfig.CommandFieldWithPresets {
		Kirigami.FormData.label: i18n("Ctrl+Scroll Down:")
		id: ctrl_mousewheel_down
	}
}
