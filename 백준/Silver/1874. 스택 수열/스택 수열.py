import sys

def solve():
    n = int(sys.stdin.readline())
    target_sequence = [int(sys.stdin.readline()) for _ in range(n)]

    stack = []
    operations = []
    count = 1
    possible = True

    for num in target_sequence:
        while count <= num:
            stack.append(count)
            operations.append('+')
            count += 1

        if stack[-1] == num:
            stack.pop()
            operations.append('-')
        else:
            possible = False
            break

    if possible:
        for op in operations:
            print(op)
    else:
        print("NO")

solve()