steps = 2017
def spinlock(n):
    pos = 0
    size = 1
    buffer = [0]
    for i in range(1, steps+1):
        pos = (pos + n) % size
        #print('pos', pos)
        buffer.insert(pos+1, i)
        size += 1
        pos += 1
        print(buffer, pos, buffer[pos])

    return buffer [(pos+1)%size]

assert spinlock(3) == 638

print('ans', spinlock(329))