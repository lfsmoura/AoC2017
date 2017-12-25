from functools import reduce

def rev(arr, mov, pos):
    """
        (0 1 2) 3 4, mov = 3, pos = 0 -> (2 1 0) 3 4
        2 1) 0 (3 4, mov = 3, pos = 3 -> 4 3) 0 (1 2
    """
    r = list(arr)
    for i in range(mov):
        r[(pos + i) % len(arr)] = arr[(pos + mov - i - 1) % len(arr)]
    return r

def tie(lenghts, n=256):
    skipsize = 0
    pos = 0
    arr = list(range(n))
    for _ in range(64):
        for mov in lenghts:
            arr = rev(arr, mov, pos)
            pos += mov + skipsize
            skipsize += 1
    r = [ reduce(lambda s, x: s ^ x, arr[i*16:(i+1)*16]) for i in range(256//16)]
    assert len(r) == 16
    r = map(lambda x : '{:02x}'.format(x), r)
    return ''.join(r)

def tie_binary(r):
    ascii = [ord(str(s)) for s in r] 
    print('run for', r)
    res = tie(ascii + [17, 31, 73, 47, 23])
    print('x',res)
    assert len(res) == len('a2582a3a0e66e6e86e3812dcb672a272')
    return res

assert tie_binary('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert tie_binary('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert tie_binary('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert tie_binary('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

input = ','.join(map(str,[197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63]))
print('x', tie_binary(input))