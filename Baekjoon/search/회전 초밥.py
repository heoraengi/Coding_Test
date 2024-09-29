import sys

N, d, k, c = map(int, sys.stdin.readline().split())
belt = []
for _ in range(N):
    belt.append(int(sys.stdin.readline().strip()))

res = 0
for i in range(N):
    if 0 <= i < N and i+k-1 < N:
        temp = belt[i:i+k]
    else:
        temp = belt[i:] + belt[:(i+k)%N]

    res = max(res, len(set(temp + [c])))

print(res)
