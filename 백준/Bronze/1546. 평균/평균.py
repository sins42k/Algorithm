n = int(input())
nums = list(map(int, input().split()))
new = []
for i in range(n) :
    new.append(nums[i]/max(nums)*100)
print(sum(new) / n)