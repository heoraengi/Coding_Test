import sys


def bs(lst, target):
    s, e = 0, n-1
    while s <= e:
        mid = (s+e) // 2
        if lst[mid] == target:
            return 1
        elif lst[mid] > target:
            e = mid - 1
        else:
            s = mid + 1

    return 0


n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))
n_lst.sort()
m = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))

for mn in m_lst:
    print(bs(n_lst, mn))
