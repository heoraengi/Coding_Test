import sys


def change(num):
    switch[num] = 0 if switch[num] == 1 else 1
    return


n = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
student_num = int(sys.stdin.readline())
for _ in range(student_num):
    student, num = map(int, sys.stdin.readline().split())

    if student == 1:
        i = 1
        while n >= num * i:
            change((num*i)-1)
            i += 1

    else:
        idx = num -1
        change(idx)
        i = 1
        while num - i >= 1 and num + i <= n :
            if switch[idx - i] == switch[idx + i]:
                change(idx - i)
                change(idx + i)
                i += 1
            else:
                break


for i in range(n):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0:
        print()
