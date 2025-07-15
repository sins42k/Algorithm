import sys

num = int(sys.stdin.readline().strip())
result = []

for i in range(num) :
    o = sys.stdin.readline().strip().split()
    if o[0] == "push" : result.append(o[1])
    elif o[0] == "pop" :
        if len(result) != 0: print(result.pop(0))
        else: print(-1)
    elif o[0] == "size" : print(len(result))
    elif o[0] == "empty" :
        if len(result) == 0 : print(1)
        else : print(0)
    elif o[0] == "front" :
        if len(result) != 0 : print(result[0])
        else : print(-1)
    elif o[0] == "back" :
        if len(result) != 0 : print(result[-1])
        else : print(-1)