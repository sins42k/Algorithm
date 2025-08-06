import sys

S1, S2 = map(int, sys.stdin.readline().split())

if S1 * 2 >= S2: print('E')
else: print('H')