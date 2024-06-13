import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
dic = dict()
start, end = 0, 0
while end < N:
    if arr[end] not in dic:
        dic[arr[end]] = 0

    if dic[arr[end]] != K:
        dic[arr[end]] += 1
        end += 1

    else:
        dic[arr[start]] -= 1
        start += 1

    cnt = max(cnt, end-start)

print(cnt)
