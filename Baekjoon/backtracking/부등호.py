k = int(input())
arr = list(input().split())
result = []
visited = [False] * 10

def check(a, b, sign):
    if (sign == '<' and a < b) or (sign == '>' and a > b) :
        return True
    else:
        return False

def back(idx, lst):
    if len(lst) == k+1:
        result.append(lst)
        return

    for i in range(10):
        if not visited[i]:
            if idx==0 or check(lst[idx-1], str(i), arr[idx-1]):
                visited[i] = True
                back(idx+1, lst + str(i))
                visited[i] = False


back(0, '')

result.sort()
print(result[-1])
print(result[0])
