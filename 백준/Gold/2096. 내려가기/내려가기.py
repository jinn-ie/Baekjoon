import sys
input = sys.stdin.readline

# input 받기
n = int(input())
start = list(map(int, input().split()))
dpmax = start
dpmin = start[:]

for i in range(1, n):
    # 한 줄씩 받을 때마다 계산
    numbers = list(map(int, input().split()))
    
    # 최댓값
    dp = dpmax[:]
    dpmax[0] = max(dp[0], dp[1]) + numbers[0]
    dpmax[1] = max(dp[0], dp[1], dp[2]) + numbers[1]
    dpmax[2] = max(dp[1], dp[2]) + numbers[2]

    # 최솟값
    dp = dpmin[:]
    dpmin[0] = min(dp[0], dp[1]) + numbers[0]
    dpmin[1] = min(dp[0], dp[1], dp[2]) + numbers[1]
    dpmin[2] = min(dp[1], dp[2]) + numbers[2]

print(max(dpmax), min(dpmin))
