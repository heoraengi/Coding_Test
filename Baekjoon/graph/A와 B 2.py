import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()
check = 0


def dfs(s, t):
    global check
    if t == s:
        check = 1
        return

    if len(t) == 0:
        return

    if t[-1] == 'A':
        dfs(s, t[:-1])

    if t[0] == 'B':
        dfs(s, t[1:][::-1])


dfs(S, T)
print(check)
