import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
res = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
graph = []
start = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)
    for j in range(M):
        if tmp[j] == 2:
            start.append([i, j])

q = deque(start)
while q:
    y, x = q.popleft()
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if visited[ny][nx] == 0 and graph[ny][nx] == 1:
                res[ny][nx] = res[y][x] + 1
                q.append([ny, nx])
                visited[ny][nx] = 1

for i in range(N):
    for j in range(M):
        if res[i][j] == 0 and graph[i][j] == 1:
            print(-1, end=' ')
        else:
            print(res[i][j], end=' ')
    print()
