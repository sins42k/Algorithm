number = int(input())
size = list(map(int, input().split()))
tshirt, pencil = map(int, input().split())
bundle = 0

for i in size :
    if i == 0 :
        continue
    elif i <= tshirt :
        bundle += 1
    elif i % tshirt == 0 :
        bundle += i//tshirt
    else :
        bundle += (i//tshirt)+1

print(bundle)
print(number//pencil, number%pencil)