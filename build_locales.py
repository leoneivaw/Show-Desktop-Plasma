import os
import subprocess
import shutil

languages = ["pt_BR", "es", "fr", "ar", "nl", "de", "it", "ru", "zh_CN", "ja", "ko", "pl", "tr", "hi"]

if not os.path.exists("contents/locale"):
    os.makedirs("contents/locale")

# copy template to each if not exists, and msgmerge
for lang in languages:
    po_file = f"translate/{lang}.po"
    if not os.path.exists(po_file):
        shutil.copy("translate/template.pot", po_file)
        # Fix the header of the copied pot file so msgfmt doesn't complain about charset
        with open(po_file, "r") as f:
            content = f.read()
        content = content.replace("charset=CHARSET", "charset=UTF-8")
        with open(po_file, "w") as f:
            f.write(content)
            
    subprocess.run(["msgmerge", "-U", po_file, "translate/template.pot"])

# compile them to locale
for lang in languages:
    po_file = f"translate/{lang}.po"
    out_dir = f"contents/locale/{lang}/LC_MESSAGES"
    os.makedirs(out_dir, exist_ok=True)
    out_file = f"{out_dir}/plasma_applet_org.kde.plasma.powershowdesktop.mo"
    subprocess.run(["msgfmt", "-o", out_file, po_file])

print("Translation compiled successfully!")
