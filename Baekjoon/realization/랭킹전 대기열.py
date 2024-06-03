import sys

p, m = map(int, sys.stdin.readline().split())
rooms = []
for _ in range(p):
    l, n = sys.stdin.readline().split()
    if len(rooms) == 0:
        rooms.append([[l, n]])

    else:
        check = False
        for room in rooms:
            if len(room) < m and int(room[0][0]) - 10 <= int(l) <= int(room[0][0]) + 10:
                room.append([l, n])
                check = True
                break
        if not check:
            rooms.append([[l, n]])

for room in rooms:
    room.sort(key=lambda x: x[1])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for r in room:
        print(' '.join(r))
