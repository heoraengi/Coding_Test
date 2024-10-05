import sys

T = int(sys.stdin.readline())

for _ in range(T):
    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())

    cnt_dic = {}
    for c in W:
        if c in cnt_dic:
            cnt_dic[c] +=1
        else:
            cnt_dic[c] = 1

    check = False
    max_result = -1
    min_result = len(W)
    check_dic = {}

    for i in range(len(W)):
        if cnt_dic[W[i]] < K:
            continue
        check = True

        if W[i] in check_dic:
            check_dic[W[i]].append(i)
        else:
            check_dic[W[i]] = [i]

    for k, n in check_dic.items():
        for i in range(len(n)-K+1):
            max_result = max(max_result, n[i+K-1] - n[i] + 1)
            min_result = min(min_result, n[i+K-1] - n[i] + 1)

    if check:
        print(min_result, max_result)
    else:
        print(-1)
