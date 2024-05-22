from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    team_dic = defaultdict(list)
    rank = list(map(int, input().split()))
    del_team = []

    # 참가 인원 수 6명 이하 제외
    for i in set(rank):
        if rank.count(i) < 6:
            del_team.append(i)

    new_rank = [i for i in rank if i not in del_team]
    for i in range(1, len(new_rank)+1):
        team_dic[new_rank[i-1]].append(i)

    # 1등 팀 선정
    result = 0
    min_rank = float('inf')
    for k, v in team_dic.items():
        if min_rank > sum(v[:4]):
            min_rank = sum(v[:4])
            result = k
        elif min_rank == sum(v[:4]):
            if team_dic[result][4] > v[4]:
                result = k

    print(result)

