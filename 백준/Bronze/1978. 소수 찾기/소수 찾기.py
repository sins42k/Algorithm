num = int(input())
prime = list(map(int, input().split()))
cnt = 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in prime :
    if is_prime(i):
        cnt += 1
    else:
        continue
    
print(cnt)