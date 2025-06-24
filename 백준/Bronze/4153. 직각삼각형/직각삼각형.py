while True :
    listNum = list(map(int, input().split()))
    if sum(listNum) == 0:
        break
    listMax = max(listNum)
    listNum.remove(listMax)
    if listNum[0]**2 + listNum[1]**2 == listMax**2 :
        print('right')
    else :
        print('wrong')