from collections import deque

N = int(input())
board = [[0]*N for _ in range(N)]
x, y = 0, 0
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        board[i][j] = temp[j]
        if temp[j] == 9:
            x = i
            y = j

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(a, b):
    visited = [[0]*N for _ in range(N)]
    queue = deque([[a, b]])
    lst = []

    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if board[a][b] > board[nx][ny] and board[nx][ny] != 0:
                    visited[nx][ny] = visited[x][y] + 1
                    lst.append((visited[nx][ny]-1, nx, ny))
                elif board[a][b] == board[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                elif board[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

    return sorted(lst, key=lambda x: (x[0], x[1], x[2]))


size = [2, 0]
cnt = 0
while True:
    board[x][y] = size[0]
    lst = deque(bfs(x,y))

    if not lst:
        break

    step, nx, ny = lst.popleft()
    cnt += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    board[x][y] = 0
    x, y = nx, ny

print(cnt)
