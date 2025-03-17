import sys
input = sys.stdin.readline

n, m = map(int, input().split())
group = [i for i in range(n)]
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])

    if group[u-1] != group[v-1]:
        g = group[v-1]
        for i in range(n):
            if group[i] == g:
                group[i] = group[u-1]

print(len(set(group)))