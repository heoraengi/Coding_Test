def solution(participant, completion):
    dic = {}
    answer = ''

    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1

    for c in completion:
        dic[c] -= 1

    for k, v in dic.items():
        if v >= 1:
            answer = k

    return answer