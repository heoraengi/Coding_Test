s = list(input())
half_1 = s.count('1')//2
half_0 = s.count('0')//2
lst_0 = [i for i in range(len(s)) if s[i] == '0']
lst_1 = [i for i in range(len(s)) if s[i] == '1']

lst_0 = lst_0[:half_0]
lst_1 = lst_1[half_1:]
for i in range(len(s)):
    if i in lst_0:
        print('0', end='')
    elif i in lst_1:
        print('1', end='')
