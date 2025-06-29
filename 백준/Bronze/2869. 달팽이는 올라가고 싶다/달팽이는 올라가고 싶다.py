A, B, V = map(int, input().split())
yh = V-B
dh = A-B

if yh % dh == 0 :
    print(yh//dh)
else :
    print((yh//dh)+1)