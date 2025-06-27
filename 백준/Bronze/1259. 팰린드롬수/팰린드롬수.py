while True :
    k = input()
    if k == '0' : break 
    else :
        if k[::-1] == k : print('yes')
        else : print('no')