num = int(input())
price_list = []

for _ in range(num) :
    k = int(input())
    if k == 0 : price_list.pop()
    elif k != 0 : price_list.append(k)

print(sum(price_list))