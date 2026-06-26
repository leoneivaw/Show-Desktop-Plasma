import glob
for file in glob.glob("translate/*.po*"):
    with open(file, "r") as f:
        content = f.read()
    content = content.replace('"Last-Translator:\n"', '"Last-Translator: \\n"\n')
    content = content.replace('"Language-Team:\n"', '"Language-Team: \\n"\n')
    with open(file, "w") as f:
        f.write(content)
