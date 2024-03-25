from collections import deque


def solution(priorities, location):
    new_list = []
    for i in range(len(priorities)):
        new_list.append([i, priorities[i]])

    queue = deque(new_list)
    max_num = max(q[1] for q in queue)
    end_list = []
    while queue:
        num = queue.popleft()
        if len(queue) == 0:
            end_list.append(num)
            break
        if num[1] == max_num:
            max_num = max(q[1] for q in queue)
            end_list.append(num)
        else:
            queue.append(num)

    cnt = 1
    for idx, num in end_list:
        if idx == location:
            break
        else:
            cnt += 1
    return cnt
