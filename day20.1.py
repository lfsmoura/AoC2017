example = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"""

import sys
import re

inp = sys.stdin.readlines()

def parse(s):
    r = list(map(int, re.findall(r'([-+]?\d+)', s)))
    return tuple(r[:3]), tuple(r[3:6]), tuple(r[6:])
    
def man(vec):
    return sum(map(abs, vec))

def char(p):
    return tuple(man(vec) for vec in p)

def sumv(a, b):
    return tuple(map(lambda a, b: a + b, a, b))

def update_point(p):
    p, v, a = p
    v = sumv(v, a)
    return (sumv(v, p), v, a)

def update(points):
    return [update_point(p) for p in points]

def left(pstr):
    points = list(map(parse, pstr))
    #print(points)
    for i in range(40000000):
        points = update(points)
        points.sort()

        collisions = set()
        for j, p1 in enumerate(points):
            for k, p2 in enumerate(points):
                if j != k and p1[0] == p2[0]:
                    collisions.add(j)
                    collisions.add(k)

        points = [ p for j, p in enumerate(points) if j not in collisions]
        #print(points)
        if i % 100 == 0:
            print(i, len(points))

    return len(points)

assert parse("p=< 3,0,0>, v=< 2,0,-190>, a=<-1,0,0>") == ((3,0,0), (2,0,-190), (-1,0,0))
#assert left(example.split('\n')) == 1

print("ans", left(inp))