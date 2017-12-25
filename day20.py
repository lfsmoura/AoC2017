example = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"""

import sys
import re

inp = sys.stdin.readlines()

# a, v, p
def parse(s):
    r = list(map(int, re.findall(r'([-+]?\d+)', s)))
    return r[6:], r[3:6], r[:3]
    
def man(vec):
    return sum(map(abs, vec))

def char(p):
    return tuple(man(vec) for vec in p)

def closest(pstr):
    points = list(map(parse, pstr))
    mini = 0
    for i, p in enumerate(points):
        print (i, p, char(p))
        if char(p) < char(points[mini]):
            mini = i
    return mini

#assert parse("p=< 3,0,0>, v=< 2,0,-190>, a=<-1,0,0>") == ([3,0,0], [2,0,-190], [-1,0,0])
assert closest(example.split('\n')) == 0

print("ans", closest(inp))