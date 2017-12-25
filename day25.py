"""
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
"""


from collections import defaultdict

def turing(p, state, steps):
    pos = 0
    tape = defaultdict(int)
    for i in range(steps):
        w,mov,state = p[state][tape[pos]]
        tape[pos] = w
        pos += mov


    return sum ( value for key,value in tape.items())
r = 1
l = -1
ex = {
    "a": {
        0: (1,r,"b"),
        1: (0,l,"b"),
    },
    "b": {
        0: (1,l,"a"),
        1: (1,r,"a"),
    }
}

assert turing(ex, "a", 6) == 3

inp = {
    "a": {
        0: (1,r,"b"),
        1: (0,l,"b"),
    },
    "b": {
        0: (1,l,"c"),
        1: (0,r,"e"),
    },
    "c": {
        0: (1,r,"e"),
        1: (0,l,"d"),
    },
    "d": {
        0: (1,l,"a"),
        1: (1,l,"a"),
    },
    "e": {
        0: (0,r,"a"),
        1: (0,r,"f"),
    },
    "f": {
        0: (1,r,"e"),
        1: (1,r,"a"),
    },
}

print(turing(inp, "a", 12683008 ))