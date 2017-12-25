ex = """..#
#..
..."""

inp = """.#...#.#.##..##....##.#.#
###.###..##...##.##....##
....#.###..#...#####..#.#
.##.######..###.##..#...#
#..#..#..##..###...#..###
..####...#.##.#.#.##.####
#......#..####..###..###.
#####.##.#.#.##.###.#.#.#
.#.###....###....##....##
.......########.#.#...#..
...###.####.##..###.##..#
#.#.###.####.###.###.###.
.######...###.....#......
....##.###..#.#.###...##.
#.###..###.#.#.##.#.##.##
#.#.#..###...###.###.....
##..##.##...##.##..##.#.#
.....##......##..#.##...#
..##.#.###.#...#####.#.##
....##..#.#.#.#..###.#..#
###..##.##....##.#....##.
#..####...####.#.##..#.##
####.###...####..##.#.#.#
#.#.#.###.....###.##.###.
.#...##.#.##..###.#.###.."""

from collections import defaultdict

"""
Clean nodes become weakened.
Weakened nodes become infected.
Infected nodes become flagged.
Flagged nodes become clean.

0    1    2    3
c -> W -> i -> f
"""

def virus(board, bursts=10000):
    m = defaultdict(bool)
    for i, line in enumerate(board.split("\n")):
        for j, char in enumerate(list(line)):
            m[(j,i)] = 2 if char == "#" else 0
    
    y, x = i // 2, j // 2
    
    dirs = [(0,-1), (-1,0), (0,1), (1,0)]
    dir = 0
    inf = 0
    while bursts > 0:
        #print(x, y, m[(x,y)], dirs[dir], inf)
        bursts -= 1

        """
        If it is clean, it turns left.
        If it is weakened, it does not turn, and will continue moving in the same direction.
        If it is infected, it turns right.
        If it is flagged, it reverses direction, and will go back the way it came.
        """

        if m[(x,y)] == 2:
            dir = (dir - 1) % 4
        elif m[(x,y)] == 1:
            inf += 1
        elif m[(x,y)] == 3:
            dir = (dir + 2) % 4
        else:
            dir = (dir + 1) % 4
        m[(x,y)] = ( m[(x,y)] + 1 ) % 4
        x += dirs[dir][0]
        y += dirs[dir][1]

    print(inf)
    return inf


assert virus(ex, 100) == 26
assert virus(ex, 10000000) == 2511944

print(virus(inp, 10000000))