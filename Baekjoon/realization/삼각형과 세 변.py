while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    lst = [a, b, c]
    lst.sort()
    if lst[2] < lst[0] + lst[1]:
        if a == b == c:
            print('Equilateral')
        elif a == b or b == c or a == c:
            print('Isosceles ')
        else:
            print('Scalene')

    else:
        print('Invalid')
