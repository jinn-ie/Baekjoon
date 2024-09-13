import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    one, two, three = 1, 2, 4
    
    # 초기값일 때
    if n == 1: print(one)
    elif n == 2: print(two)
    elif n == 3: print(three)
    # 그 이상일 때 점화식 사용
    else:
        for i in range(n - 3):
            one, two, three = two, three, one + two + three
        print(three)