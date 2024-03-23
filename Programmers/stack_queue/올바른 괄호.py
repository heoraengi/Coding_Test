def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0 or c == '(':
            stack.append(c)
        elif stack[-1] == '(' and c == ')':
            stack.pop()

    return True if len(stack) == 0 else False
