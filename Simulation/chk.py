import re, sys
def headers(p):
    t = re.sub(r'\n\+', ' ', open(p).read())
    return {l.split()[1]: l.split()[2:] for l in t.splitlines()
            if l.split() and l.split()[0].lower() == '.subckt'}
mine, pdk = headers(sys.argv[1]), headers(sys.argv[2])
for n, pins in sorted(mine.items()):
    if n.startswith('gf180mcu') and n in pdk and pdk[n] != pins:
        print('MISMATCH', n, '\n  macro:', pins, '\n  pdk  :', pdk[n])
