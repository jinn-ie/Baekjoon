import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]

res = 0

for y in range(n):
    for x in range(m):
        if paint[y][x] != 0:
            color = paint[y][x]
            # 오른쪽으로 진행하며
            for i in range(m - x):
                # 색칠해야 하는 구역 체크
                if paint[y][x + i] != 0:
                    # 같은 색상이면 덧칠할 필요 없으므로 방문 체크
                    if paint[y][x + i] == color:
                        paint[y][x + i] = 0
                # 0을 만나면 색칠 끝
                else:
                    res += 1
                    break
            # 오른쪽 끝에 도달하면 색칠 끝
            else: res += 1


print(res)