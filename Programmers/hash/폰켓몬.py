def solution(nums):
    n1 = len(nums)//2
    n2 = len(set(nums))
    return n2 if n1 >= n2 else n1