import sys

def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)
        for _ in range(n):
            x_str = sys.stdin.readline()
            if not x_str:
                break
            x = int(x_str)
            if x % 2 == 0:
                print(f"{x} is even")
            else:
                print(f"{x} is odd")
    except (IOError, ValueError) as e:
        pass

solve()
