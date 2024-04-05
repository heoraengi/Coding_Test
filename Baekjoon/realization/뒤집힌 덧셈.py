def rev(n):
    r = ''
    while n > 0:
        r += str(n%10)
        n = n//10
    return int(r)


x, y = map(int, (input().split()))
print(rev(rev(x) + rev(y)))
