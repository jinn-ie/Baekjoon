import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
locations = list(map(int, input().split()))

height = max(locations[0], n - locations[-1])
for i in range(m - 1):
    if (locations[i + 1] - locations[i] + 1) // 2 > height:
        height = (locations[i + 1] - locations[i] + 1) // 2

print(height)