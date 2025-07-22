num = int(input())
word = input()
s = b = 0

for i in range(num) :
    if word[0] == 's' : 
        s += 1
        word = word[8:]
    else :
        b += 1
        word = word[7:]

if s == b : print("bigdata? security!")
elif s > b : print("security!")
else : print("bigdata?")