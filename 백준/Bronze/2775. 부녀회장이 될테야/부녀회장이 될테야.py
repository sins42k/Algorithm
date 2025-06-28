t = int(input())
apartment = [[0] * 15 for _ in range(15)]
for i in range(1, 15):
    apartment[0][i] = i
for ii in range(1, 15):
    for iii in range(1, 15):
        apartment[ii][iii] = apartment[ii][iii-1] + apartment[ii-1][iii]
for _ in range(t):
    k = int(input())
    n = int(input())
    print(apartment[k][n])