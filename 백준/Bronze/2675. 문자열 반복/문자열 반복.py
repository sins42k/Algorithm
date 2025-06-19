num = int(input())

for i in range(num) :
    number, character = map(str, input().split())
    int(number)
    list(character)

    for ii in range(len(list(character))) :
        print(list(character)[ii] * int(number), end='')

    print(" ")