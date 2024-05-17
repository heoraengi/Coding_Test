import sys

n, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

sorted_board = sorted(board, key=lambda x: (-x[1], -x[2], -x[3]))

idx = [x[0] for x in sorted_board].index(k)

for i in range(n):
    if sorted_board[i][1:] == sorted_board[idx][1:]:
        print(i+1)
        break
