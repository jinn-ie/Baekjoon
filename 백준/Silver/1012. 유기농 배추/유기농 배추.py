import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())

    ground = [[0 for _ in range(m)] for _ in range(n)]
    worm = 0

    # 땅 세팅
    for _ in range(k):
        x, y = map(int, input().split())
        ground[y][x] = 1

    for i in range(n):              # y
        for j in range(m):          # x
            # 새 땅 발견
            if ground[i][j] == 1:
                worm += 1
                stack = [[i, j]]
                ground[i][j] = 0

                while stack:
                    # DFS
                    y, x = stack.pop()
                    # 사방탐색
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        # 자식 노드 발견
                        if 0 <= nx < m and 0 <= ny < n and ground[ny][nx] == 1:
                            ground[ny][nx] = 0
                            stack.append([ny, nx])

    print(worm)
