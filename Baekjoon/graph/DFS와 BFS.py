from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

new_graph = [sorted(g) for g in graph]


def bfs(g, visit, v):
    res = []
    q = deque([[v]])
    while q:
        node = q.popleft()
        for n in node:
            if visit[n] == 0:
                visit[n] = 1
                q.append(g[n])
                res.append(n)
    return res


def dfs(g, visit, v, res):
    res.append(v)
    visit[v] = 1
    for i in g[v]:
        if visit[i] == 0:
            dfs(g, visit, i, res)

    return res


print(' '.join(map(str, (dfs(new_graph, visited_dfs, V, [])))))
print(' '.join(map(str, (bfs(new_graph, visited_bfs, V)))))
