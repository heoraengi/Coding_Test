def solution(sizes):
    max_h = 0
    max_w = 0

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if max_w < sizes[i][0]:
            max_w = sizes[i][0]
        if max_h < sizes[i][1]:
            max_h = sizes[i][1]

    return max_h * max_w
