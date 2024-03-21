from collections import deque


def solution(arr):
    q = deque(arr)
    stack = []
    top = 0
    stack.append(q.popleft())

    while q:
        num = q.popleft()
        if stack[top] != num:
            stack.append(num)
            top += 1

    return stack