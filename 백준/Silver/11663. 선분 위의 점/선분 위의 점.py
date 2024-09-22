import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()

def binary_search(lr, target):
    start, end = 0, len(dots) - 1

    while start <= end:
        cur = (start + end) // 2
        if dots[cur] < target:      start = cur + 1
        elif dots[cur] > target:    end = cur - 1
        else:                       return cur

    # L, R에 따라 선분 내의 점을 반환하기 위한 처리
    if lr == 0:     return start
    elif lr == 1:   return end

# 매 선분 정보마다 계산
for _ in range(m):
    start, end = map(int, input().split())

    left = binary_search(0, start)
    right = binary_search(1, end)

    print(right - left + 1)