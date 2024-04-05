import sys

n, k = map(int, sys.stdin.readline().split())
diff = n-k
number = sys.stdin.readline().rstrip()

stack = []
for num in number:
    while stack and stack[-1] < num and k >0:
        stack.pop()
        k -=1
    stack.append(num)

result = ''
for i in range(diff):
    result += stack[i]

print(result)
