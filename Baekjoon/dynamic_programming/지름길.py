import sys

N, D = map(int, sys.stdin.readline().split())
dp = [i for i in range(D+1)]
hipass = []

for i in range(N):
    s, e, k = map(int, sys.stdin.readline().split())
    if e - s > k:
        hipass.append([s, e, k])

hipass.sort()

for s, e, k in hipass:
    for i in range(D+1):
        if e == i:
            dp[i] = min(dp[i], dp[s] + k)
        else:
            dp[i] = min(dp[i], dp[i-1]+1)

print(dp[D])




