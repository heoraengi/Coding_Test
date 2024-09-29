import sys

n = int(sys.stdin.readline())
balls = sys.stdin.readline().strip()
red = balls.count('R')
blue = n - red
res = min(red, blue)

cnt = 0

for i in range(n):
    if balls[0] != balls[i]:
        break
    cnt += 1

if balls[0] == 'R':
    res = min(res, red - cnt)
else:
    res = min(res, blue - cnt)

cnt = 0

for i in range(n-1, -1, -1):
    if balls[-1] != balls[i]:
        break
    cnt += 1

if balls[-1] == 'R':
    res = min(res, red - cnt)
else:
    res = min(res, blue - cnt)

print(res)


