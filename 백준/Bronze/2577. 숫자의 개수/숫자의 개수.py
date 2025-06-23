a = int(input())
b = int(input())
c = int(input())
num = a*b*c
charNum =  str(num)
listNum = []
for i in range(len(charNum)) :
    listNum.append(charNum[i:i+1])
for ii in range(0, 10) :
    k = listNum.count(str(ii))
    print(k)