alphabet = input().upper()
set_alphabet = list(set(alphabet))

cnt_alphabet = []
for alpha in set_alphabet:
    cnt = alphabet.count(alpha)
    cnt_alphabet.append(cnt)

if cnt_alphabet.count(max(cnt_alphabet)) >= 2:
    print('?')
else:
    print(set_alphabet[cnt_alphabet.index(max(cnt_alphabet))])
