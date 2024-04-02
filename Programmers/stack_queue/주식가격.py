from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        time = 0
        price = prices.popleft()

        for p in prices:
            time += 1
            if price > p:
                break

        answer.append(time)

    return answer
