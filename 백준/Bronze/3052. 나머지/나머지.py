listNum = []
for i in range(10) :
    k = int(input())
    listNum.append(k % 42)
check = len(set(listNum))
print(check)