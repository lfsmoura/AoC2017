ex = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""

inputa = """14/42
2/3
6/44
4/10
23/49
35/39
46/46
5/29
13/20
33/9
24/50
0/30
9/10
41/44
35/50
44/50
5/11
21/24
7/39
46/31
38/38
22/26
8/9
16/4
23/39
26/5
40/40
29/29
5/20
3/32
42/11
16/14
27/49
36/20
18/39
49/41
16/6
24/46
44/48
36/4
6/6
13/6
42/12
29/41
39/39
9/3
30/2
25/20
15/6
15/23
28/40
8/7
26/23
48/10
28/28
2/13
48/14"""

import re
from collections import defaultdict

def strongest(inp):
    g = defaultdict(list)
    id = 0
    for line in inp.split("\n"):
        a,b = map(int, re.findall(r"(\d+)", line))
        id += 1
        g[a].append((a,b,id))
        g[b].append((b,a,id))
    print(g)
    def depth(node, cost=0, visited=None):
        visited = {} if not visited else visited
        if node[2] in visited:
            return 0
        visited[node[2]] = True
        #print(node, g[node])
        r = [cost]
        for n in g[node[1]]:
            r.append(depth(n, cost + n[0] + n[1], dict(visited)))
        print (node, r)
        return max(r)

    r = depth((0,0,0))
    print(r)
    return r

assert strongest(ex) == 31

print("ans", strongest(inputa))