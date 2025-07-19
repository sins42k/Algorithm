import sys
from collections import deque

def solve():
    test_cases = int(sys.stdin.readline())

    for _ in range(test_cases):
        n, m = map(int, sys.stdin.readline().split())
        priorities = list(map(int, sys.stdin.readline().split()))
        
        queue = deque([(p, i) for i, p in enumerate(priorities)])
        
        print_count = 0
        
        while queue:
            current_doc = queue.popleft()
            current_priority = current_doc[0]
            current_index = current_doc[1]
            
            if any(current_priority < other_doc[0] for other_doc in queue):
                queue.append(current_doc)
            else:
                print_count += 1
                if current_index == m:
                    print(print_count)
                    break

solve()
