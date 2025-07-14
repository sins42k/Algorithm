import sys

num1 = int(sys.stdin.readline())
list1 = sys.stdin.readline().split()

counts = {}
for i in list1:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

num2 = int(sys.stdin.readline())
list2 = sys.stdin.readline().split()

result = []
for i in list2:
    result.append(str(counts.get(i, 0)))

print(" ".join(result)) 