import sys

def solve():
    a = int(sys.stdin.readline())
    w, v = map(int, sys.stdin.readline().split())

    if w / v >= a:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    solve()
