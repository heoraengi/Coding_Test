import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    n = int(sys.stdin.readline())

    if len(heap) == 0 and n == 0:
        print(0)

    elif n == 0:
        print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, n)

