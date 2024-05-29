T = int(input())

for _ in range(T):
    n, k, t, mn = map(int, input().split())
    score = [[0]*k for _ in range(n)]
    submit = [0] * n
    submit_time = [0] * n

    for m in range(mn):
        i, j, s = map(int, input().split())
        score[i-1][j-1] = max(s, score[i-1][j-1])
        submit[i-1] +=1
        submit_time[i-1] = m
    result = []
    for x in range(n):
        result.append([x+1, sum(score[x]), submit[x], submit_time[x]])

    result.sort(key=lambda x: (-x[1], x[2], x[3]))

    for x in range(n):
        if result[x][0] == t:
            print(x+1)
            break
