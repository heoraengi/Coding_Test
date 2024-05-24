import sys

n, x = map(int, sys.stdin.readline().split())
visitant = list(map(int, sys.stdin.readline().split()))

if max(visitant) == 0:
    print('SAD')
else:
    max_visit = sum(visitant[:x])
    value = max_visit
    cnt = 1
    for i in range(x, n):
        value += visitant[i]
        value -= visitant[i-x]

        if max_visit < value:
            max_visit = value
            cnt = 1
        elif max_visit == value:
            cnt += 1

    print(max_visit)
    print(cnt)
