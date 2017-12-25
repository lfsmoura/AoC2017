import re

def dance(crew, moves=None):
    n = len(crew)
    for move in moves:
        if move[0] == 's':
            s = int(re.search(r's(\d+)', move).group(1))
            crew = crew[-s:] + crew[:-s]
        elif move[0] == 'x':
            x = re.search(r'x(\d+)/(\d+)', move)
            a, b = int(x.group(1)), int(x.group(2))
            crew = list(crew)
            crew[a], crew[b] = crew[b], crew[a]
            crew = ''.join(crew)
        elif move[0] == 'p':
            p = re.search(r'p([a-p])/([a-p])', move)
            a, b = p.group(1), p.group(2)
            crew = crew.replace(a, 'z')
            crew = crew.replace(b, a)
            crew = crew.replace('z', b)
        else:
            raise Exception()
    assert len(crew) == n
    assert len(set(list(crew))) == n
    return crew


import sys
mvs = sys.stdin.readlines()[0].split(',')

cer = []
rec = {}
billion = 1000000000
crew = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[:16]
for i in range(billion):
    crew = dance(crew, moves=mvs)
    if crew in rec:
        print(i)
        print(rec[crew])
        print(cer[(billion % i) - 1])
        break

    rec[crew] = i
    cer.append(str(crew))

