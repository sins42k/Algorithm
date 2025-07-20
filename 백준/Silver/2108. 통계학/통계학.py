import sys
from collections import Counter

n = int(sys.stdin.readline())

numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

mean = round(sum(numbers) / n)
print(mean)

numbers.sort()
median = numbers[n // 2]
print(median)

counts = Counter(numbers).most_common(2)

if len(counts) == 1 or counts[0][1] != counts[1][1]:
    mode = counts[0][0]
else:
    mode = counts[1][0]
print(mode)

range_val = numbers[-1] - numbers[0]
print(range_val)
