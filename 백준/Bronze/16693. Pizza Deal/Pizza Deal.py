import math
a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

slicePizza = a1 / p1
wholePizza = (math.pi * r1 * r1) / p2

if slicePizza > wholePizza : print("Slice of pizza")
else : print("Whole pizza")