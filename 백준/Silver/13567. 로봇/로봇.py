import sys
input = sys.stdin.readline

m, n = map(int, input().split())
x, y = 0, 0
direction = 0

for _ in range(n):
    command, num = input().split()
    if command == "TURN":                               # TURN
        if num == "0":  direction = (direction + 1) % 4
        else:           direction = (direction + 3) % 4
    else:                                               # MOVE
        if direction == 0:      x += int(num)           # 동
        elif direction == 1:    y += int(num)           # 북
        elif direction == 2:    x -= int(num)           # 서
        else:                   y -= int(num)           # 남
        
        if not (0 <= x <= m and 0 <= y <= m):
            print(-1)
            break
else: print(x, y)