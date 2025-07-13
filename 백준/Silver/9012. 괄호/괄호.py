num = int(input())

for _ in range(num):
    parenthesis = input()
    stack = 0
    is_valid = True
    
    for char in parenthesis:
        if char == '(':
            stack += 1
        elif char == ')':
            stack -= 1
            if stack < 0:  # 닫는 괄호가 더 많은 경우
                is_valid = False
                break
    
    if stack == 0 and is_valid:
        print("YES")
    else:
        print("NO")