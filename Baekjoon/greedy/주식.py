import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))

    result = 0
    max_money = 0
    for i in range(N-1, -1, -1):
        if lst[i] > max_money:
            max_money = lst[i]
        else:
            result += max_money - lst[i]

    print(result)
