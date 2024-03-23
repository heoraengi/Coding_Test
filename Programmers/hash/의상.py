from collections import defaultdict


def solution(clothes):
    hash_map = defaultdict(list)
    for name, types in clothes:
        hash_map[types].append(name)

    # hash_map ={}
    # for name, types in clothes:
    #     if types in hash_map :
    #         hash_map[types].append(name)
    #     else :
    #         hash_map[types] = [name]

    total = 1
    for k, v in hash_map.items():
        total *= len(v) + 1

    return total - 1
