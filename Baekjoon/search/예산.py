import sys
n = int(sys.stdin.readline())
costs = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())
start, end = 0, max(costs)

while start <= end:
    mid = (start+end)//2
    total = 0
    for c in costs:
        if c > mid:
            total += mid
        else:
            total += c
    if budget >= total:
        start = mid + 1
    else:
        end = mid - 1

print(end)
