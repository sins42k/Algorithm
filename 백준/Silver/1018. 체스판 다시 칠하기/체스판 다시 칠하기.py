import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().strip() for _ in range(n)]
    min_repaints = 64

    for start_row in range(n - 7):
        for start_col in range(m - 7):
            repaints1 = 0
            repaints2 = 0

            for r in range(start_row, start_row + 8):
                for c in range(start_col, start_col + 8):
                    if (r + c) % 2 == 0:
                        if board[r][c] != 'W':
                            repaints1 += 1
                        if board[r][c] != 'B':
                            repaints2 += 1
                    else:
                        if board[r][c] != 'B':
                            repaints1 += 1
                        if board[r][c] != 'W':
                            repaints2 += 1
            
            current_min = min(repaints1, repaints2)
            if current_min < min_repaints:
                min_repaints = current_min

    print(min_repaints)

if __name__ == "__main__":
    solve()
