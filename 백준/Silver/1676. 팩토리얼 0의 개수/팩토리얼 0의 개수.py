n = int(input())

def factorial(n):
       if n == 0:
           return 1
       else:
           return n * factorial(n-1)

k = factorial(n)
k = str(k)
k = list(k)
k.reverse()

cnt = 0

for i in k :
    if i == '0' : cnt += 1
    else : break

print(cnt)