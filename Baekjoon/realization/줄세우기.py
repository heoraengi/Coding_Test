import sys

p = int(sys.stdin.readline())
for _ in range(p):
    temp = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    min_num = temp[1]
    for i in range(1,len(temp)-1):
        for j in range(i+1, len(temp)):
            if temp[i] > temp[j]:
                temp[i], temp[j] = temp[i],temp[j]
                cnt +=1

    print(temp[0], cnt)
