heart_x = 0
heart_y = 0
end_waist = 0
head = False

left_arm = 0
right_arm = 0
left_leg = 0
right_leg = 0
waist = 0

# 입력
n = int(input())
board = [[] for _ in range(n)]
for i in range(n):
    temp = input().strip()
    for j in range(n):
        board[i].append(temp[j])
        if not head and temp[j] == '*':
            # 심장 위치 찾기
            heart_x = i+1
            heart_y = j
            head = True

# 팔 계산
for i in range(n):
    if board[heart_x][i] == '*':
        if i < heart_y:
            left_arm += 1
        elif i > heart_y:
            right_arm += 1

# 허리 계산
for i in range(heart_x+1, n):
    if board[i][heart_y] == '*':
        waist += 1
    else:
        end_waist = i
        break

# 다리 계산
for i in range(end_waist, n):
    if board[i][heart_y-1] == '*':
        left_leg += 1
    else:
        break

for i in range(end_waist, n):
    if board[i][heart_y+1] == '*':
        right_leg += 1
    else:
        break


# 출력 부분
print(heart_x+1, heart_y+1)
print(left_arm, right_arm, waist, left_leg, right_leg)