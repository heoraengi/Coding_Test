N = int(input())
lst = list(map(int, input().split()))
stack = []
result = [-1] * N

for i in range(N):
    while stack and lst[stack[-1]] < lst[i]:
        result[stack.pop()] = lst[i]
    stack.append(i)

for r in result:
    print(r, end=' ')
