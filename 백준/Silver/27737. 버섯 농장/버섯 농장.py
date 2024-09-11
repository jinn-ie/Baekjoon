import sys
input = sys.stdin.readline

# 상하좌우 방향 배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

board = []

# input
n, m, k = map(int, input().split())
for _ in range(n):
    board.append(list(map(int, input().split())))
nm = m

for i in range(n):                                  # y
    for j in range(n):                              # x
        if board[i][j] == 0:
            ground = 1
            board[i][j] = 1
            # DFS
            stack = [[i, j]]
            while stack:
                y, x = stack.pop()
                for l in range(4):                  # 사방 탐색
                    ny, nx = y + dy[l], x + dx[l]
                    if -1 < ny < n and -1 < nx < n:
                        if board[ny][nx] == 0:
                            ground += 1
                            board[ny][nx] = 1
                            stack.append([ny, nx])

            nm += (-ground // k)                     # ceil 대신 음수 몫 사용
            # 포자 초과 사용
            if nm < 0:
                print("IMPOSSIBLE")
                break
    else: continue                                  # 이중 반복문 탈출
    break           
else:
    # 포자를 사용하지 않음
    if m == nm :
        print("IMPOSSIBLE")
    # 농사 가능
    else:
        print("POSSIBLE")
        print(nm)