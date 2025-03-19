from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [False] * 100001
running = True

if n == k:
    print(0)
    running = False    

# BFS
queue = deque([[n, 0]])
while running:
    i, t = queue.popleft()
    t += 1
    tmp = [i + 1, i - 1, i * 2]
    for j in tmp:
        if j == k:
            print(t)
            running = False
        elif 0 <= j <= 100000 and not visited[j]:
            visited[j] = True
            queue.append([j, t])
    