from collections import deque
import sys
input = sys.stdin.readline

# input
N = int(input())
stones = list(map(int, input().split()))
a, b = map(int, input().split())
a -= 1                      # index와 징검다리 번호 일치시킴
b -= 1

# 변수 설정
queue = deque([a])
depth = [0] * N
visited = [False] * N
visited[a] = True

# BFS
while queue:
    cur = queue.popleft()
    # index가 0 이상 N 미만인 동안 탐색
    for i in range (cur - (cur // stones[cur]) * stones[cur], N, stones[cur]):
        # 해가 아닐 때 큐에 추가
        if not visited[i]:
            queue.append(i)
            depth[i] = depth[cur] + 1
            visited[i] = True
        # 해일 때 depth 출력
        if i == b:
            depth[i] = depth[cur] + 1
            print(depth[i])
            break
    else: continue          # 이중 반복문 탈출을 위함
    break
else: print(-1)