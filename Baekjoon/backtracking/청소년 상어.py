from copy import deepcopy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
board = []
for i in range(4):
    temp = list(map(int, input().split()))
    box = []
    for j in range(4):
        box.append([temp[2*j], temp[2*j+1]-1])
    board.append(box)

max_cnt = 0

def dfs(x, y, cnt, board):
    global max_cnt
    cnt += board[x][y][0]
    max_cnt = max(max_cnt, cnt)
    board[x][y][0] = 0

    for fish in range(1, 17):
        fx, fy = -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == fish:
                    fx, fy = i, j
                    break

        if fx == -1 and fy == -1:
            continue

        fd = board[fx][fy][1]

        for i in range(8):
            nd = (fd+i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]

            if not (0<= nx <4 and 0<= ny< 4) or (nx == x and ny == y):
                continue
            board[fx][fy][1] = nd
            board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
            break


    sd = board[x][y][1]
    for i in range(1, 5):
        nx = x + dx[sd]*i
        ny = y + dy[sd]*i

        if 0<= nx <4 and 0<=ny < 4 and board[nx][ny][0] > 0:
            dfs(nx, ny, cnt, deepcopy(board))


dfs(0,0,0, board)
print(max_cnt)

