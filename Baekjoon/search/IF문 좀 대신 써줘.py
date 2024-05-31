n, m = map(int, input().split())
levels = []
for _ in range(n):
    a, b = input().split()
    levels.append([a, int(b)])

powers = []
for _ in range(m):
    powers.append(int(input()))


def bs(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid][1] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return start


for power in powers:
    print(levels[bs(levels, power, 0, n-1)][0])


