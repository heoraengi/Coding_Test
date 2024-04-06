n = int(input())
arr = list(map(int, input().split()))
max_num = 0


def back(visited, lst):
    global max_num

    if len(lst) == n:
        total = 0
        for i in range(n-1):
            total += abs(lst[i] - lst[i+1])
        max_num = max(max_num, total)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            back(visited, lst + [arr[i]])
            visited[i] = False


visited = [False] * n
back(visited, [])

print(max_num)
