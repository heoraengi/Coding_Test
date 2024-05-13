def solution(n, computers):
    def dfs(i, visited, computers):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j, visited, computers)

    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            cnt += 1

    return cnt

## BFS
from collections import deque


def solution(n, computers):
    def bfs(i, visited, computers):
        queue = deque([i])
        visited[i] = True

        while queue:
            q = queue.popleft()
            for j in range(n):
                if computers[q][j] == 1 and not visited[j]:
                    queue.append(j)
                    visited[j] = True

    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers)
            cnt += 1

    return cnt