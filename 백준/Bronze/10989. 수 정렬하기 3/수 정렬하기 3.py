import sys

num = int(sys.stdin.readline())
cnt = [0] * 10001

for _ in range(num):
    cnt[int(sys.stdin.readline())] += 1

for i in range(10001):
    if cnt[i] > 0:
        for _ in range(cnt[i]):
            print(i)
