import math


def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    max_day = 0
    cnt = 0
    answer = []

    for d in days:

        if max_day == 0:
            max_day = d

        if max_day >= d:
            cnt += 1

        else:
            answer.append(cnt)
            cnt = 1
            max_day = d

    answer.append(cnt)

    return answer
