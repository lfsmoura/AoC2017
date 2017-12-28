REM = 2147483647

def pairs(n=40000000,a=0, b=0):
    fa=16807
    fb=48271
    r = 2 ** 16
    c = 0
    for i in range(n):
        a = (a * fa) % REM
        b = (b * fb) % REM
        if a % r == b % r:
            c += 1
    print c
    return c


assert pairs(n=5,a=65,b=8921) == 1
assert pairs(a=65, b=8921) == 588

print 'ans', pairs(a=289, b=629)