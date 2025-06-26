l = int(input())
alphabet = input()
stack = 0

for i in range(l) :
    stack += (ord(alphabet[i])-96) * (31 ** i)
print(stack)