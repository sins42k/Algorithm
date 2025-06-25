num = int(input())
k = 0
for i in range(num) :
    listNum = list(map(int, str(i)))
    
    if num == sum(listNum) + i : 
        k = i
        break
print(k)
