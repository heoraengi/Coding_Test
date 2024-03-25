from collections import deque


def is_visited(nx, ny, visited, maps, row, col):
    return 0 <= nx < col and 0 <= ny < row and not visited[ny][nx]  and maps[ny][nx] == 1


def solution(maps):
    row, col = len(maps), len(maps[0])
    visited = [[False] * col for _ in range(row)]
    visited[0][0] = True
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque([(0, 0, 1)])

    while q:
        x, y, cnt = q.popleft()
        if x == col - 1 and y == row - 1:
            return cnt

        for i in range(4):
            if is_visited(x + dx[i], y + dy[i], visited, maps, row, col):
                q.append((x + dx[i], y + dy[i], cnt + 1))
                visited[y + dy[i]][x + dx[i]] = True

    return -1