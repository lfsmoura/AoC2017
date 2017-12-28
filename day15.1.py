REM = 2147483647

def pairs(n=5000000,a=0, b=0):
    fa=16807
    fb=48271
    r = 2 ** 16
    c = 0
    for i in range(n):
        while True:
            a = (a * fa) % REM
            if a % 4 == 0:
                break
        while True:
            b = (b * fb) % REM
            if b % 8 == 0:
                break
        if a % r == b % r:
            c += 1
    print c
    return c


assert pairs(n=1056,a=65,b=8921) == 1
#assert pairs(a=65, b=8921) == 309

print 'ans', pairs(a=289, b=629)