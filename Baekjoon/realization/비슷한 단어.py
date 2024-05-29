import sys

n = int(sys.stdin.readline())
standard = list(sys.stdin.readline().strip())
cnt = 0
for i in range(n-1):
    word = list(sys.stdin.readline().strip())
    copy_standard = standard[:]
    for w in standard:
        if w in word:
            word.remove(w)
            copy_standard.remove(w)

    if len(word) <= 1 and len(copy_standard) <= 1:
        cnt += 1

print(cnt)

