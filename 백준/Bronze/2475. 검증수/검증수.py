i, ii, iii, iv, v = map(int, input().split())

listVI = [i, ii, iii, iv, v]

vi = 0

for i in listVI :
    vi += i ** 2

print(vi%10)