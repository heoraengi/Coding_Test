N = int(input())
columns = []
for i in range(N):
    columns.append(list(map(int, input().split())))

columns.sort()
max_height = 0
max_height_idx = 0
for i in range(N):
    if max_height < columns[i][1]:
        max_height = columns[i][1]
        max_height_idx = i

res = 0
curr_height = columns[0][1]
for i in range(max_height_idx):
    res += (columns[i + 1][0] - columns[i][0]) * curr_height
    if curr_height < columns[i+1][1]:
        curr_height = columns[i+1][1]

curr_height = columns[-1][1]
for i in range(N-1, max_height_idx, -1):
    res += (columns[i][0] - columns[i - 1][0]) * curr_height
    if curr_height < columns[i-1][1]:
        curr_height = columns[i-1][1]


print(res + max_height)
