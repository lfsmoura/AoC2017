from collections import defaultdict

arr = defaultdict(int)
arr[(0,0)] = 1
def s(i, j):
    return sum(arr[(y, x)] for (y, x) in [(i-1,j-1), (i-1,j), (i-1, j+1), (i, j-1), (i,j+1), (i+1,j-1), (i+1, j), (i+1,j+1)])

d = {
    "first": 2,
    "bpq": 2
}
i, j = 0, 0
target = 289326
bpq = 0
for level in range(1, 100):
    print ("level", level)
    bpq += 2
    j += 1
    i += 1
    # primeiro quadrante
    for mi, mj in [(-1,0), (0,-1), (1,0), (0,1)]:
        for k in range(0, bpq):
            i += mi
            j += mj
            arr[(i, j)] = s(i, j)
            print(arr[(i, j)])
            if arr[(i, j)] > target:
                print("answer :",arr[(i, j)])
                exit(0)