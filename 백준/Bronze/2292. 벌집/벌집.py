n = int(input())
i = 1
stack = 1
while n > stack :
    stack += 6*i
    i += 1
print(i)