import sys
from collections import deque

input = sys.stdin.readline

num = int(input())
cards = deque(range(1, num + 1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
