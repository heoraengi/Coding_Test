def solution(answers):
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    answer = []

    for i in range(3):
        cnt = 0
        num = len(pattern[i])
        for a in range(len(answers)):
            if answers[a] == pattern[i][a % num]:
                cnt += 1
        answer.append([i + 1, cnt])

    answer.sort(key=lambda x: -x[1])

    result = []
    max_num = answer[0][1]
    for i, n in answer :
        if n == max_num :
            result.append(i)

    return result

print(solution([1,3,2,4,2]))
