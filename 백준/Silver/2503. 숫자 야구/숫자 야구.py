import sys
input = sys.stdin.readline

nums = []

# 숫자 리스트 생성
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and k != i:
                nums.append(str(i) + str(j) + str(k))

# input 받기
n = int(input())
for _ in range(n):
    guess, strike, ball = input().split()
    strike, ball = int(strike), int(ball)
    
    delete = []

    # nums의 모든 수에 대해 가능 여부 확인
    for num in nums:
        s, b = 0, 0
        # 각 자리마다 확인
        for i in range(3):
            if num[i] in guess:
                if num[i] == guess[i]:  s += 1
                else:                   b += 1
        if s != strike or b != ball:    delete.append(num)
    for d in delete: nums.remove(d)

print(len(nums))