import sys
input = sys.stdin.readline

# input 받기
n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

# 맨 위쪽은 왼쪽 값 합산
for j in range(1, m):
    ground[0][j] += ground[0][j - 1]

for i in range(1, n):
    # 맨 왼쪽은 위쪽 값 합산
    ground[i][0] += ground[i - 1][0] 
    for j in range(1, m):
        # 그 외는 왼쪽, 위쪽 중 큰 값 합산
        ground[i][j] += max(ground[i - 1][j], ground[i][j - 1])

print(ground[n - 1][m - 1])