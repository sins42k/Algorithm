numbers = list(map(int, input().split()))
a = 0
d = 0
for i in range(len(numbers)) :
    if numbers[i] == (i+1) : a += 1
    else : break

for i in range(len(numbers)) :
    if numbers[i] == (len(numbers)-i) : d += 1
    else : break

if a == 8 :
    print('ascending')
elif d == 8 :
    print('descending')
else :
    print('mixed')