import sys
input = sys.stdin.readline

# 상하좌우 방향 배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

paint = []
visited = []


def count_zone():

    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):                      # y
        for j in range(n):                  # x
            if not visited[i][j]:
                visited[i][j] = 1
                count += 1
                # DFS
                stack = [[i, j]]
                while stack:
                    y, x = stack.pop()
                    # 사방 탐색
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        # 그림 범위 내인지 확인
                        if -1 < ny < n and -1 < nx < n:
                            if not visited[ny][nx]:
                                if paint[ny][nx] == paint[y][x]:
                                    visited[ny][nx] = 1
                                    stack.append([ny, nx])
    
    return count


def main():
    
    # input 받기
    global n
    n = int(input())
    for _ in range(n):
        paint.append(input())

    # 비적록색약 그림 탐색
    normal = count_zone()

    # 적록색약 그림으로 수정
    for i in range(n):
        paint[i] = paint[i].replace("G", "R").rstrip()

    # 적록색약 그림 탐색
    weakness = count_zone()

    print(normal, weakness)

main()