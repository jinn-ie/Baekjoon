import sys
input = sys.stdin.readline

# input 받기
n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

# 맨 아래는 오른쪽 값 합산
for j in range(m - 2, -1, -1):
    ground[n - 1][j] += ground[n - 1][j + 1]

for i in range(n - 2, -1, -1):
    # 맨 오른쪽은 아래 값 합산
    ground[i][m - 1] += ground[i + 1][m - 1] 
    for j in range(m - 2, -1, -1):
        # 그 외는 오른쪽, 아래 중 큰 값 합산
        ground[i][j] += max(ground[i + 1][j], ground[i][j + 1])

print(ground[0][0])