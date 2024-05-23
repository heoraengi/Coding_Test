from collections import deque

n = int(input())

cards = [i for i in range(1, n+1)]

q = deque(cards)

while True:
    if len(q) == 1:
        break
    q.popleft()
    q.append(q.popleft())

result = q.popleft()
print(result)
