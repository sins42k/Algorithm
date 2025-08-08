num1 = int(input())
num2 = input()

for i in reversed(range(len(num2))) :
    print(num1 * int(num2[i]))
print(num1 * int(num2))