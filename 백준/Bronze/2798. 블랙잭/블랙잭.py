from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))
sums = {sum(comb) for comb in combinations(cards, 3) if sum(comb) <= m}
print(max(sums))