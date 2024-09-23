import sys
input = sys.stdin.readline

# input 받기
n,m = map(int,input().split())
woods = list(map(int,input().split()))

# 초깃값 설정
low = 0
high = max(woods)

# 이분탐색
while low <= high:
    # 초깃값 설정
    h = (low + high) // 2
    get = 0

    # 나무 잘라보기
    for wood in woods:
        if wood > h: get += wood - h
        if get > m:
            low = h + 1
            break
    else:
        if get == m:
            print(h)
            break
        else: high = h - 1
else:
    if high == h - 1: print(h - 1)
    else: print(h)