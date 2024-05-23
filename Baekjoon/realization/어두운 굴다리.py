def bs(lights, mid):
    if lights[1]-lights[0] > mid:
        return 0
    if lights[-1]-lights[-2] > mid:
        return 0
    for i in range(1, len(lights)-2):
        if (lights[i+1] - lights[i])/2 > mid:
            return 0
    return 1


n = int(input())
m = int(input())
lights = [0] + list(map(int, input().split())) + [n]
height = 0
s, e = 0, n

while s <= e:
    m = (s+e) // 2
    if bs(lights, m):
        e = m - 1
        height = m
    else:
        s = m + 1

print(height)
