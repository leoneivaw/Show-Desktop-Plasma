import re

po_file = "translate/pt_BR.po"
with open(po_file, "r", encoding="utf-8") as f:
    po = f.read()

replacements = {
    'msgid "Use Icon instead of colors"\nmsgstr ""': 'msgid "Use Icon instead of colors"\nmsgstr "Usar Ícone em vez de cores"'
}

for old, new in replacements.items():
    po = po.replace(old, new)

with open(po_file, "w", encoding="utf-8") as f:
    f.write(po)
