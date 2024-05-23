import sys

n, m = map(int, sys.stdin.readline().split())
words = dict()
for i in range(n):
    word = sys.stdin.readline().rstrip()
    # words[word].append([1, len(word)])
    if len(word) >= m:
        if word in words:
            words[word][0] += 1
        else:
            words[word]= [1, len(word)]

words = sorted(words.items(), key=lambda x:(-x[1][0], -x[1][1], x[0]))

for key, _ in words:
    print(key)