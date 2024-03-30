from collections import defaultdict


def solution(genres, plays):
    answer = []
    dic = defaultdict(list)

    for i in range(len(genres)):
        dic[genres[i]].append([i, plays[i]])

    dic_sort = {}

    for genre in dic:
        dic_sort[genre] = sorted(dic[genre], key=lambda x: -x[1])

    list_keys = []
    for k, values in dic.items():
        total = 0
        for v in values:
            total += v[1]
        list_keys.append([k, total])
    list_keys.sort(key=lambda x: -x[1])

    for i, _ in list_keys:
        count = 0
        for v in dic_sort[i]:
            if count > 1:
                break
            else:
                answer.append(v[0])
                count += 1

    return answer
