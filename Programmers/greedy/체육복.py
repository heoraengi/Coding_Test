def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    new_lost = []
    for l in lost:
            if l in reserve:
                reserve.remove(l)
            else :
                new_lost.append(l)

    for r in reserve:
        for l in new_lost:
            if r - 1 == l or r + 1 == l:
                new_lost.remove(l)
                break

    return n - len(new_lost)
