import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

stars = [[' ' for _ in range(n * 2 - 1)] for _ in range(n)]

def draw(x, y, cnt):
    if cnt == 0:
        stars[y][x] = '*'
        stars[y + 1][x - 1], stars[y + 1][x + 1] = '*', '*'
        for i in range(5): stars[y + 2][x - 2 + i] = '*'
    else:
        draw(x, y, cnt // 2)
        draw(x - cnt * 3, y + cnt * 3, cnt // 2)
        draw(x + cnt * 3, y + cnt * 3, cnt // 2)

draw(n - 1, 0, n // 6)

# 별 출력
for i in range(n):
    for j in range(n * 2 - 1):
        print("%s" % stars[i][j])
    print("\n")