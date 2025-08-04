atk_a, hp_a = map(int, input().split())
atk_b, hp_b = map(int, input().split())

while True:
    hp_a -= atk_b
    hp_b -= atk_a

    if hp_a <= 0 and hp_b <= 0:
        print("DRAW")
        break
    elif hp_b <= 0:
        print("PLAYER A")
        break
    elif hp_a <= 0:
        print("PLAYER B")
        break
