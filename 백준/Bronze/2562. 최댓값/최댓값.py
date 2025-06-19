numList = []
for i in range(1, 10) :
    num = int(input())
    numList.append(num)

maxInt = 0

for j in range(len(numList)) :
    if max(numList) == numList[j] :
        maxInt += j+1

print(max(numList))
print(maxInt)