n, play = input().split()
player = set()
for i in range(int(n)):
    player.add(input())

if play == 'Y':
    print(len(player))
elif play == 'F':
    print(len(player)//2)
else:
    print(len(player)//3)

