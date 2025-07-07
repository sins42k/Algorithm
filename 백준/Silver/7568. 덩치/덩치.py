n = int(input())

big = []
grade = []

for i in range(n):
    a, b = map(int, input().split())
    big.append((a, b))
 
for i in range(n):
    count = 0
    for j in range(n):
        if big[i][0] < big[j][0] and big[i][1] < big[j][1]:
            count += 1 
    grade.append(count + 1)
 
for d in grade:
    print(d,end=" ")
