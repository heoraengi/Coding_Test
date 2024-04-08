import sys

n = int(sys.stdin.readline())
step = [0] * 301
for i in range(1, n+1):
    step[i] = int(sys.stdin.readline())

dp = [0] * 301
dp[1] = step[1]
dp[2] = step[2] + step[1]
if n > 2:
    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + step[i], dp[i-3] + step[i-1] + step[i])

print(dp[n])
