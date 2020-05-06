import os


def make_safe_for_katex(line):
    line = line.replace(r'\(', r'$`')
    line = line.replace(r'\)', r'`$')
    line = line.replace(r'\begin{align*}', r'\begin{aligned}')
    line = line.replace(r'\end{align*}', r'\end{aligned}')
    line = line.replace(r'\begin{align}', r'\begin{aligned}')
    line = line.replace(r'\end{align}', r'\end{aligned}')
    line = line.replace(r'\begin{eqnarray}', r'\begin{aligned}')
    line = line.replace(r'\end{eqnarray}', r'\end{aligned}')
    line = line.replace(r'\begin{eqnarray*}', r'\begin{aligned}')
    line = line.replace(r'\end{eqnarray*}', r'\end{aligned}')
    return line


for filename in os.listdir("docs"):
    if filename.endswith(".md"):
        fin = open(f"docs/{filename}", 'rt')
        fout = open(f"convdocs/{filename}", 'w')

        cond = False

        for line in fin:
            if '$$' in line:
                if cond:
                    fout.write(line.replace('$$', '```'))
                    cond = False
                else:
                    fout.write(line.replace('$$', '```math'))
                    cond = True
            else:
                fout.write(make_safe_for_katex(line))
        fin.close()
        fout.close()
