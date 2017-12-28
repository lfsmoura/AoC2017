
grid = []

with open("input.txt") as f:
    for line in f.readlines():
        grid.append(line)

test = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""

tgrid = [ line for line in test.split('\n')]


def seq(g):
    w = len(g[0])
    h = len(g)
    y, x = 0, g[0].index('|')
    down = (0,1)
    up = (0,-1)
    left = (-1, 0)
    right = (1, 0)
    dir = down
    res = []
    print g[y], y, x
    print "------------>", g[y][x]
    while x >= 0 and x < w and y >= 0 and y < h: 
        x += dir[0]
        y += dir[1]
        #print dir, y, x
        print g[y][x]
        if g[y][x] == " ":
            break
        elif g[y][x] in ["|", "-", "\t"]:
            pass
        elif g[y][x] == "+":
            if dir is up or dir is down:
                if g[y][(x-1)%w] != ' ':
                    dir = left
                else:
                    dir = right
            else:
                if g[(y-1)%h][x] != ' ':
                    dir = up
                else:
                    dir = down
        else:
            res.append(g[y][x])


    return ''.join(res)
assert seq(tgrid) == "ABCDEF"

# TWBPYAQFUQAYPBWTV
print 'ans', seq(grid)