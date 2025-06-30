isbn = input()
check = int(isbn[-1])
weight = 0
cnt = 0

for i, ii in zip(isbn[:-1], [1, 3]*6) :
    if i == '*' :
        cnt = ii
        continue
    weight += int(i) * ii

for iii in range(10) :
    k = weight + (iii*cnt) + check
    if k % 10 == 0 : print(iii)
    else : continue