num = int(input())

zeros = [0] * 41
ones = [0] * 41
zeros[0] = 1
ones[0] = 0
zeros[1] = 0
ones[1] = 1

for i in range(2, 41) :
    zeros[i] = zeros[i-1] + zeros[i-2]
    ones[i] = ones[i-1] + ones[i-2]

for ii in range(num) :
    n = int(input())
    print(zeros[n], ones[n])