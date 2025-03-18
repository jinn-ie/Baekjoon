from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())

graph = []
result = []
visited = set()

for i in range(n):
    tmp = list(map(int, input().split()))
    if 2 in tmp: start = [i, tmp.index(2)]
    graph.append(tmp)
    minus = []
    for j in range(m):
        minus.append(-tmp[j])
    result.append(minus)

result[start[0]][start[1]] = 0
queue = deque([start])

while queue:
    y, x = queue.popleft()
    graph[y][x] = -1 # visited

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 1:
                if result[ny][nx] == -1:
                    result[ny][nx] = result[y][x] + 1
                else:
                    result[ny][nx] = min(result[ny][nx], result[y][x] + 1)
                if (ny, nx) not in visited:
                    queue.append([ny, nx])
                    visited.add((ny, nx))
                
    
for i in range(n):
    print(*result[i])