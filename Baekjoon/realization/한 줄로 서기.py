N = int(input())
lst = list(map(int, input().split()))
res = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == lst[i] and res[j] == 0:
            res[j] = i+1
            break
        elif res[j] == 0:
            cnt += 1

for r in res:
    print(r, end=' ')

