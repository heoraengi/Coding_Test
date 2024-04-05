name = input()
n = int(input())
teams = []
for i in range(n):
    teams.append(input())
teams.sort()

dic = {'L':0, 'O':0, 'V':0, 'E':0}
for c in name:
    if c in dic:
        dic[c] +=1
lst = [dic.copy() for _ in range(n)]

for i in range(n):
    for t in teams[i]:
        if t in lst[i]:
            lst[i][t] += 1

mod_list = []

for d in lst:
    cal = ((d['L']+d['O'])*(d['L']+d['V'])*(d['L']+d['E'])*(d['O']+d['V'])*(d['O']+d['E'])*(d['V']+d['E']))%100
    mod_list.append(cal)

print(teams[mod_list.index(max(mod_list))])
