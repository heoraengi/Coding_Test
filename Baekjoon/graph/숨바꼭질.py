from collections import deque

n, k = map(int, input().split())
q = deque([n])
MAX = 10**5
visit = [0] * (MAX+1)
while q:
    x = q.popleft()
    if x == k:
        print(visit[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= MAX and visit[nx] == 0:
            visit[nx] = visit[x] + 1
            q.append(nx)
