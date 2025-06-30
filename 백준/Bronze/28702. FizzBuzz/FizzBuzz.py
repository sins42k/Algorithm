fb = ['Fizz', 'Buzz', 'FizzBuzz']
for i in range(3, 0, -1) :
    k = input()
    if k not in fb :
        n = int(k) + i
        break
if n % 3 == 0 and n % 5 == 0 : print(fb[2])
elif n % 5 == 0 : print(fb[1])
elif n % 3 == 0 : print(fb[0])
else : print(n)