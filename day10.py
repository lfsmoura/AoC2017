

def rev(arr, mov, pos):
    """
        (0 1 2) 3 4, mov = 3, pos = 0 -> (2 1 0) 3 4
        2 1) 0 (3 4, mov = 3, pos = 3 -> 4 3) 0 (1 2

2 1) 0 (3 4
2 1) 0 (3 4

    """
    r = list(arr)
    for i in range(mov):
        r[(pos + i) % len(arr)] = arr[(pos + mov - i - 1) % len(arr)]
    print(arr, mov, pos, r)
    return r

def tie(lenghts, n=256):
    skipsize = 0
    pos = 0
    arr = list(range(n))
    for mov in lenghts:
        arr = rev(arr, mov, pos)
        pos += mov + skipsize
        skipsize += 1
    return arr[0] * arr[1]

assert tie([3, 4, 1, 5], 5) == 12

print('', tie([197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63]))