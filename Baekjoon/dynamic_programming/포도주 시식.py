n = int(input())
wine = [0]*10000
for i in range(n):
    wine[i] = int(input())

dp = [0]* 10000
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0] + wine[2], wine[1] + wine[2],  dp[1])
if n > 3:
    for i in range(3, n):
        dp[i] = max(dp[i-1], wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2])

print(dp[n-1])