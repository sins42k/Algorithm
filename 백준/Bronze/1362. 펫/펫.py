import sys

scenario_num = 0
while True:
    line = sys.stdin.readline().strip()
    if not line or line == "0 0":
        break

    scenario_num += 1
    o, w = map(int, line.split())
    is_dead = False

    while True:
        action_line = sys.stdin.readline().strip()
        if action_line == "# 0":
            break

        if is_dead:
            continue

        action, value = action_line.split()
        value = int(value)

        if action == 'F':
            w += value
        elif action == 'E':
            w -= value
            if w <= 0:
                is_dead = True

    if is_dead:
        status = "RIP"
    else:
        if o / 2 < w < o * 2:
            status = ":-)"
        else:
            status = ":-("

    print(f"{scenario_num} {status}")
