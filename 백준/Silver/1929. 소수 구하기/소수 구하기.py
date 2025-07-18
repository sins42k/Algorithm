m, n = map(int, input().split())
a = [False, False] + [True]*(n-1)

for i in range(2, int(n**0.5)+1) :
    if a[i] :
        for ii in range(i*i, n+1, i) :
            a[ii] = False

for i in range(m, n+1) :
    if a[i] :
        print(i)