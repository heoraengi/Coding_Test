n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
lst = [set() for _ in range(n)]
cnt = []
for j in range(5):
    for i in range(n):
        for k in range(n):
            if i!=k:
                if table[i][j]==table[k][j]:
                    lst[i].add(k)

for s in lst:
    cnt.append(len(s))

print(cnt.index(max(cnt)) + 1)
