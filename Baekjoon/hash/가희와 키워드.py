import sys

n, m = map(int, sys.stdin.readline().split())
keywords = dict()
for _ in range(n):
    keywords[sys.stdin.readline().strip()] = 0
cnt = 0
for _ in range(m):
    writing = list(sys.stdin.readline().strip().split(','))
    for w in writing:
        if w in keywords:
            if keywords[w] == 0:
                cnt += 1
                keywords[w] = 1
    print(n - cnt)
