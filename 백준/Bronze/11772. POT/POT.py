import sys

def solve():
  try:
    n_str = sys.stdin.readline()
    if not n_str:
      return
    n = int(n_str)
    
    total_sum = 0
    for _ in range(n):
      line = sys.stdin.readline()
      if not line:
        continue

      num_str = line.strip()
      base_str = num_str[:-1]
      exponent_str = num_str[-1]
      base = int(base_str)
      exponent = int(exponent_str)
      total_sum += base ** exponent
      
    print(total_sum)

  except (ValueError, IndexError) as e:
    pass

solve()
