import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

people_list = [i for i in range(1, n + 1)]
queue = deque(people_list)
result = []

while queue:
    queue.rotate(-(k - 1))
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")
