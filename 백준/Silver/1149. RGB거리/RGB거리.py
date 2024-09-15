import sys
input = sys.stdin.readline

# input 받기
n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]

# 초항 설정
cur = houses[0]

# DP
for i in range(1, n):
    for j in range(3):
        houses[i][j] += min(houses[i - 1][(j + 1) % 3], houses[i - 1][(j + 2) % 3])

print(min(houses[n - 1]))