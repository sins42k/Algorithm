N = int(input())
is_present = any(N in {i, j, i * j} for i in range(2, 10) for j in range(1, 10))
print(int(is_present))
