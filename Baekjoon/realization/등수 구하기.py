n, score, p = map(int, input().split())
if n == 0:
    print(1)
    exit()

rank_lst = list(map(int, input().split()))
rank_lst.append(score)
rank_lst.sort(reverse=True)

idx = rank_lst.index(score)
cnt = rank_lst.count(score)

if p >= idx + cnt:
    print(idx+1)
else:
    print(-1)