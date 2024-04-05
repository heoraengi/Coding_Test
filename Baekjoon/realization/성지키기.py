import sys

N, M = map(int, sys.stdin.readline().split())
castle = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
col = set()
row = set()
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row.add(i)
            col.add(j)

n_diff = N- len(row)
m_diff = M- len(col)

if n_diff >= m_diff:
    print(n_diff)
else:
    print(m_diff)
