import os

for filename in os.listdir("docs"):
    if filename.endswith(".md"):
        fin = open(f"docs/{filename}", 'rt')
        fout = open(f"convdocs/{filename}", 'w')

        cond = False

        for line in fin:
            if line.strip().startswith('$$'):
                if cond:
                    fout.write(line.replace('$$', '```'))
                    cond = False
                else:
                    fout.write(line.replace('$$', '```math'))
                    cond = True
            else:
                fout.write(line)
        fin.close()
        fout.close()
