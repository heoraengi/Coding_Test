import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [0] * 101
visit = [0] * 101

ladders = dict(tuple(map(int, input().split())) for _ in range(N))
snakes = dict(tuple(map(int, input().split())) for _ in range(M))

q = deque([1])
visit[1] = 1
while q:
    x = q.popleft()
    if x == 100:
        print(board[x])
        break

    for dice in range(1, 7):
        nx = x + dice
        if nx <= 100 and visit[nx] == 0:
            if nx in ladders:
                nx = ladders[nx]
            if nx in snakes:
                nx = snakes[nx]
            if visit[nx] == 0:
                visit[nx] = 1
                board[nx] = board[x] + 1
                q.append(nx)

