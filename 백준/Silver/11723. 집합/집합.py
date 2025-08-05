import sys

input = sys.stdin.readline

m = int(input())
s = 0

for _ in range(m):
    line = input().strip().split()
    command = line[0]

    if command == "add":
        x = int(line[1])
        s |= (1 << (x - 1))
    elif command == "remove":
        x = int(line[1])
        s &= ~(1 << (x - 1))
    elif command == "check":
        x = int(line[1])
        if s & (1 << (x - 1)):
            print(1)
        else:
            print(0)
    elif command == "toggle":
        x = int(line[1])
        s ^= (1 << (x - 1))
    elif command == "all":
        s = (1 << 20) - 1
    elif command == "empty":
        s = 0
