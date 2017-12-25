import sys
from functools import reduce

def divisibles(arr):
    print(arr)
    for k, a in enumerate(arr):
        for b in arr[k+1:]:
            if a % b == 0:
                return a / b
    raise NumException()

rows = map(lambda s: list(reversed(sorted(map(int, s.strip().split('\t'))))), sys.stdin.readlines())
checksum = sum( divisibles(row) for row in list(rows) )
print(checksum)
	
