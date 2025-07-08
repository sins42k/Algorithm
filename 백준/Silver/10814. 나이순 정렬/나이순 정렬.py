
num = int(input())
member_list = []

for _ in range(num):
    age, name = input().split()
    member_list.append([int(age), name])

member_list.sort(key=lambda x: x[0])

for i in member_list:
    print(i[0], i[1])