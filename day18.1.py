from collections import defaultdict

"""
snd X plays a sound with a frequency equal to the value of X.
set X Y sets register X to the value of Y.
add X Y increases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
"""

def duet(lines, pc, reg, squeue, rqueue):
    inst = [ line.split(' ') for line in lines if len(line) > 0]    
    
    def value(y):
        try:
            return int(y)
        except ValueError:
            return reg[y]

    while pc < len(inst):
        op = inst[pc][0]
        x = inst[pc][1]

        #print (inst[pc], value(x))
        if op == 'snd':
            squeue.insert(0, value(x))
        elif op == 'set':
            reg[x] = value(inst[pc][2])
        elif op == 'add':
            reg[x] += value(inst[pc][2])
        elif op == 'mul':
            reg[x] *= value(inst[pc][2])
        elif op == 'mod':
            reg[x] = reg[x] % value(inst[pc][2])
        elif op == 'rcv':
            if len(rqueue) > 0:
                reg[x] = rqueue.pop()
            else:
                return pc
        elif op == 'jgz':
            if value(x) > 0:
                pc += value(inst[pc][2])
                continue
        pc += 1

inputa = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 826
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
"""

lines = inputa.split('\n')

p1q = []
p2q = []
p1pc = 0
p2pc = 0
sent = 0
#sent_this_loop = True

reg1 = defaultdict(int)
reg2 = defaultdict(int)
reg1['p'] = 0
reg2['p'] = 1
c = 1
while True:
    c += 1
    if c > 1700:
        break
    #sent_this_loop = False
    p1pc = duet(lines, p1pc, reg1, p1q, p2q)
    #sent_this_loop = sent_this_loop or len(p1q) > 0
    assert len(p2q) == 0
    p2pc = duet(lines, p2pc, reg2, p2q, p1q)
    assert len(p1q) == 0
    #sent_this_loop = sent_this_loop or len(p2q) > 0
    sent += len(p2q)
    if len(p1q) > 0 or len(p2q) > 0:
        print(p1q, p2q)

print('sent', sent)