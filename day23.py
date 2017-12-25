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

def duet(lines):
    inst = [ line.split(' ') for line in lines if len(line) > 0]    
    reg = defaultdict(int)

    def value(y):
        try:
            return int(y)
        except ValueError:
            return reg[y]

    pc = 0
    muls = 0

    while pc < len(inst) and pc >= 0:
        op = inst[pc][0]
        x = inst[pc][1]

        print (inst[pc], value(x), pc, muls)
        if op == 'set':
            reg[x] = value(inst[pc][2])
        elif op == 'sub':
            reg[x] -= value(inst[pc][2])
        elif op == 'mul':
            muls += 1
            reg[x] *= value(inst[pc][2])
        elif op == 'jnz':
            if value(x) != 0:
                pc += value(inst[pc][2])
                print(pc, "becomes")
                continue
        pc += 1
    return muls

"""
exinput = 

assert duet(exinput.split('\n')) == 4
"""

inputa = """set b 93
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""

print(duet(inputa.split('\n')))