steps = 50000000

def spinlock(n):
    pos = 1
    size = 2
    after0 = 1
    for i in range(2, steps+1):
        pos = (pos + n) % size
        if pos == 0:
            after0 = i
            #print(after0)
        pos += 1
        size += 1
        #print(i, pos, after0)

    return after0

print('ans', spinlock(329))