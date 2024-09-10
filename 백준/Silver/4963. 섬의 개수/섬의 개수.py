from collections import deque
import sys
input = sys.stdin.readline

# 상하좌우 대각선 방향 배열
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break                             # 프로그램 종료

    land = []
    result = 0                                              # 섬의 개수

    for _ in range(h):
        land.append(list(map(int, input().split())))

    for i in range(h):                                      # y
        for j in range(w):                                  # x
            
            # 새 섬 발견
            if land[i][j] == 1:
                result += 1
                land[i][j] = 0                              # visited 대체
                stack = [[i, j]]
                
                # DFS
                while stack:
                    y, x = stack.pop()
                    for k in range(8):                      # 8방향 탐색
                        nx, ny = x + dx[k], y + dy[k]
                        if -1 < nx < w and -1 < ny < h:     # out of index 방지
                            if land[ny][nx] == 1:
                                land[ny][nx] = 0
                                stack.append([ny, nx])
    print(result)