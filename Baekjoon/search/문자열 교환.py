import sys

arr = sys.stdin.readline().strip()
a = arr.count('a')
arr += arr[:a-1]

res = float('inf')
for i in range(len(arr)-(a-1)):
    res = min(res, arr[i: i+a].count('b'))

print(res)
