import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break

    stack = []
    is_balanced = True
    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                is_balanced = False
                break
        elif char == ']':
            if not stack or stack.pop() != '[':
                is_balanced = False
                break

    if is_balanced and not stack:
        print("yes")
    else:
        print("no")
