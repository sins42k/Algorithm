import sys

def custom_round(val):
    return int(val + 0.5)
n = int(sys.stdin.readline())

if n == 0: print(0)
else:
    levels = [int(sys.stdin.readline()) for _ in range(n)]
    levels.sort()
    cut = custom_round(n * 0.15)
    
    if cut > 0: trimmed_levels = levels[cut:-cut]
    else: trimmed_levels = levels
    
    avg = sum(trimmed_levels) / len(trimmed_levels)
    print(custom_round(avg))