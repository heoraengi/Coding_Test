from collections import deque

n, k = map(int, input().split())
q = deque([n])
MAX = 10**5
visit = [0] * (MAX+1)
dist = [0] * (MAX+1)
visit[n] = 1

while q:
    x = q.popleft()

    if x == k:
        print(dist[k])
        break

    for nx in (x*2, x-1, x+1):
        if 0 <= nx <= MAX and visit[nx] == 0:
            if nx == x*2:
                dist[nx] = dist[x]
            else:
                dist[nx] = dist[x] + 1
            visit[nx] = 1
            q.append(nx)
