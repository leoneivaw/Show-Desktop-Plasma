import os

qml_file = "contents/ui/config/ConfigAdvanced.qml"
with open(qml_file, "r", encoding="utf-8") as f:
    qml = f.read()

replacements = {
    'i18n("Ctrl+Click Command:")': 'i18n("Ctrl+Click:")',
    'i18n("Middle Click Command:")': 'i18n("Middle Click:")',
    'i18n("Shift+Click Command:")': 'i18n("Shift+Click:")',
    'i18n("Alt+Click Command:")': 'i18n("Alt+Click:")'
}

for old, new in replacements.items():
    qml = qml.replace(old, new)

with open(qml_file, "w", encoding="utf-8") as f:
    f.write(qml)
