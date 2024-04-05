a, b = map(int, input().split())
arr = []

for i in range(1000):
    for j in range(i):
        arr.append(i)

total = 0
for i in range(a-1, b):
    total += arr[i]

print(total)
