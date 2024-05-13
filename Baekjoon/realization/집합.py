import sys

n = int(sys.stdin.readline())
s = set()

for i in range(n):
    temp = sys.stdin.readline().strip().split()
    if len(temp) == 1:
        if temp[0] == 'all':
            s = set(i for i in range(1, 21))

        elif temp[0] == 'empty':
            s = set()
    else:
        if temp[0] == 'add':
            s.add(int(temp[1]))

        elif temp[0] == 'remove':
            s.discard(int(temp[1]))

        elif temp[0] == 'check':
            if int(temp[1]) in s:
                print(1)
            else:
                print(0)

        elif temp[0] == 'toggle':
            if int(temp[1]) in s:
                s.discard(int(temp[1]))
            else:
                s.add(int(temp[1]))
