people, height = map(int, input().split())
people_height = list(map(int, input().split()))
people_height = [i for i in people_height if i <= height]
print(len(people_height))