import sys

n, k = map(int, sys.stdin.readline().split())
table = list(sys.stdin.readline().strip())
cnt = 0

for i in range(n):
    if table[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if table[j] == 'H':
                table[j] = 'X'
                cnt += 1
                break

print(cnt)
