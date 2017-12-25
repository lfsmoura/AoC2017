import sys
from functools import reduce

rows = map(lambda s: list(map(int, s.strip().split('\t'))), sys.stdin.readlines())
minmax = [reduce(lambda s, x: [min(s[0], x), max(s[1], x)], row, [row[0], row[0]]) for row in list(rows)]
checksum = reduce(lambda s, x: s + x[1] - x[0], minmax, 0)
print(checksum)
	
