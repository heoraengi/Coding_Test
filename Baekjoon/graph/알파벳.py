import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, visited, dist):
    global cnt

    cnt = max(cnt, dist)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and visited[board[nx][ny]] == 0:
            visited[board[nx][ny]] = 1
            dfs(nx, ny, visited, dist + 1)
            visited[board[nx][ny]] = 0

    return cnt


r, c = map(int, sys.stdin.readline().split())
board = [list(map(lambda x:ord(x)-ord('A'), sys.stdin.readline().rstrip())) for _ in range(r)]
visited = [0] * 26
visited[board[0][0]] = 1
cnt = 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

print(dfs(0,0, visited, cnt))
