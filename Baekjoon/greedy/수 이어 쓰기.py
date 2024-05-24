import sys

nums = sys.stdin.readline().strip()
idx = 0
while True:
    idx += 1
    n = str(idx)
    while len(n) > 0 and len(nums) > 0:
        if n[0] == nums[0]:
            nums = nums[1:]
        n = n[1:]
    if nums == '':
        print(idx)
        break
