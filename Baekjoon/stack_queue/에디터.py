import sys

arr = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline())
tmp = []
for _ in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L' and arr:
        tmp.append(arr.pop())

    elif command[0] == 'D' and tmp:
        arr.append(tmp.pop())

    elif command[0] == 'B' and arr:
        arr.pop()

    elif command[0] == 'P':
        arr.append(command[1])

print(''.join(arr + tmp[::-1]))

