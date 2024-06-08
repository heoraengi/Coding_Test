import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        for t in tmp:
            heapq.heappush(heap, t)
    else:
        for t in tmp:
            if heap[0] < t:
                heapq.heappop(heap)
                heapq.heappush(heap, t)

print(heap[0])
