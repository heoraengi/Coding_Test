n = int(input())
card1 = list(input().split())
m = int(input())
card2 = list(input().split())
card1.sort()


def bs(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


for c in card2:
    if bs(card1, c, 0, len(card1)-1):
        print(1, end=' ')
    else:
        print(0, end=' ')
