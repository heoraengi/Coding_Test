import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    for i in range(len(scoville)-1):
        min_v1 = heapq.heappop(scoville)
        if min_v1 >= K:
            return cnt

        min_v2 = heapq.heappop(scoville)
        value = min_v1 + min_v2 * 2
        heapq.heappush(scoville, value)
        cnt += 1

    if scoville[0] < K:
        return -1

    return cnt
