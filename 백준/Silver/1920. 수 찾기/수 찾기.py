import sys

n = int(sys.stdin.readline())
fir_set = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
sec_list = list(map(int, sys.stdin.readline().split()))

for i in sec_list:
    if i in fir_set:
        print("1")
    else:
        print("0")
