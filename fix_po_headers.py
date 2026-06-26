import glob
for file in glob.glob("translate/*.po*"):
    with open(file, "r") as f:
        lines = f.readlines()
    
    out = []
    for line in lines:
        if line.startswith('"Last-Translator:'):
            out.append('"Last-Translator: \\n"\n')
        elif line.startswith('"Language-Team:'):
            out.append('"Language-Team: \\n"\n')
        elif line == '"\n':
            # Skip stray quotes
            continue
        else:
            out.append(line)
            
    with open(file, "w") as f:
        f.writelines(out)
