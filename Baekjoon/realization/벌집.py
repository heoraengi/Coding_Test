n = int(input())
cnt = 1
start = 1
cal = 6
while True:
    if n <= start:
        print(cnt)
        break
    start += cal * cnt
    cnt +=1

