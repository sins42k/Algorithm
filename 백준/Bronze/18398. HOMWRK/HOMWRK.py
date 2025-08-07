import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    for _ in range(N):
        A, B = map(int, sys.stdin.readline().split())
        print(A + B, A * B)
