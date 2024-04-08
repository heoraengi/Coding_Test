def solution(name):
    n = len(name)
    cnt = 0

    for c in name:
        up_down = min(ord(c) - ord('A'), 26 + ord('A') - ord(c))
        cnt += up_down

    move = n - 1

    for left in range(n):
        i = left + 1
        while (i < n) and (name[i] == 'A'):
            i += 1

        right = n - i
        min_distance = min(left, right)

        move = min(move, left + right + min_distance)

    return cnt + move
