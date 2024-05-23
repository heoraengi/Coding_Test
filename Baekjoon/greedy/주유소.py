n = int(input())
dist = list(map(int, input().split()))
city = list(map(int, input().split()))
min_cost = city[0]
total = 0
for i in range(n-1):
    if min_cost > city[i]:
        min_cost = city[i]
    total += (min_cost*dist[i])

print(total)