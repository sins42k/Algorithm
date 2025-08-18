import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_by_name = {}
pokemon_by_number = {}

for i in range(1, n + 1):
    name = input().strip()
    pokemon_by_name[name] = i
    pokemon_by_number[i] = name

for _ in range(m):
    query = input().strip()
    if query.isdigit(): print(pokemon_by_number[int(query)])
    else: print(pokemon_by_name[query])
