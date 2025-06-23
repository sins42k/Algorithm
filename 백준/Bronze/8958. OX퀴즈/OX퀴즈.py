num = int(input())
for i in range(num) :
    ox = str(input())
    k = 0
    cnt = 1
    for ii in range(len(ox)) :
        if list(ox)[ii] == 'O' :
            k += cnt
            cnt += 1
        else :
            cnt = 1
    print(k)