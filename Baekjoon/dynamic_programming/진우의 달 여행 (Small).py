n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [-1, 0, 1]


def dfs(x, y, d, min_fuel, curr):
    if y == n-1:
        return min(min_fuel, curr)
    for i in direction:
        if i != d:
            nx = i + x
            if 0 <= y < n and 0 <= nx < m:
                min_fuel = dfs(nx, y+1, i, min_fuel, curr + board[y+1][nx])

    return min_fuel


min_fuel = float('inf')
for i in range(m):
    min_fuel = min(dfs(i, 0, 3, min_fuel, board[0][i]), min_fuel)

print(min_fuel)






