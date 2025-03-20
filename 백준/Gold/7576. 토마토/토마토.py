from collections import deque
import sys
input = sys.stdin.readline

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

box = []
queue = deque()

# input
m, n = map(int, input().split())
for i in range(n):
    tmp = list(map(int, input().split()))
    box.append(tmp)
    queue.extend([[i, j, 0] for j in range(len(tmp)) if tmp[j] == 1])
    # == for j in range(len(tmp)):
    #        if tmp[j] == 1:
    #            queue.append([i, j, 0])

# BFS
while queue:
    y, x, t = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx< m and box[ny][nx] == 0:
            box[ny][nx] = -1
            queue.append([ny, nx, t + 1])

# output
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit()
else: print(t)