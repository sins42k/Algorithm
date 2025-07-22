people = list(input().split())
apple = list(input().split())

if apple[0] in people : print((people.index(apple[0]))+1)
elif apple[0] not in people : print(0)