num = []
for i in range(3) :
    num.append(int(input()))
print(num[0] + num[1] - num[2])
strNum = str(num[0]) + str(num[1])
print(int(strNum) - num[2])