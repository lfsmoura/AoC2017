import re

def dance(n=16, moves=None):
    crew = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[:n]
    for move in moves:
        if move[0] == 's':
            s = int(re.search(r's(\d+)', move).group(1))
            print(s)

            crew = crew[-s:] + crew[:-s]
        elif move[0] == 'x':
            x = re.search(r'x(\d+)/(\d+)', move)
            a, b = int(x.group(1)), int(x.group(2))
            crew = list(crew)
            crew[a], crew[b] = crew[b], crew[a]
            crew = ''.join(crew)
            print ('x', a, b)
        elif move[0] == 'p':
            p = re.search(r'p([a-p])/([a-p])', move)
            a, b = p.group(1), p.group(2)
            crew = crew.replace(a, 'z')
            crew = crew.replace(b, a)
            crew = crew.replace('z', b)
            print('p', a, b)
        else:
            raise Exception()
        print('01234567890123456')
        print(crew, move)
    assert len(crew) == n
    assert len(set(list(crew))) == n
    return crew

assert dance(5, ['s3']) == "cdeab"
assert dance(5, ['s4']) == "bcdea"
assert dance(5, ['s5']) == "abcde"
assert dance(5, ['s1', 'x3/4', 'pe/b']) == 'baedc'
import sys
mvs = sys.stdin.readlines()[0].split(',')
print("ans", dance(moves=mvs))