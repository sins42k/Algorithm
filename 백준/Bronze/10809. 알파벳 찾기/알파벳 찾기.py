s = str(input())
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
listNum = []
for i in range(len(alphabet)) :
    if alphabet[i] in list(s) :
        l = s.find(alphabet[i])
        listNum.append(l)
    else :
        listNum.append(-1)
for ii in range(len(listNum)) :
    print(listNum[ii], end=' ')