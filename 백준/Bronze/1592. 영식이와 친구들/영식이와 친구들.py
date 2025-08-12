N, M, L = map(int, input().split())
ball = [1] + [0] * (N - 1)
idx = 0
 
if M == 1:
    print(0)
else:
    while 1:
        if ball[idx] % 2 == 1:
            idx += L
        else:
            idx -= L
 
        if idx >= N:
            idx %= N
        elif idx < 0:
            idx += N
 
        ball[idx] += 1
 
        if ball[idx] == M:
            break
 
    print(sum(ball) - 1)