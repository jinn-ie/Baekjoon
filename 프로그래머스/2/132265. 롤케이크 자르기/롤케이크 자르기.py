def solution(topping):
    answer = 0
    n = len(topping)
    
    left_set = set()
    right_set = set()
    
    left_cnt = [0] * n
    right_cnt = [0] * n
    
    for i in range(n):
        # 왼쪽 누적
        left_set.add(topping[i])
        left_cnt[i] = len(left_set)
        
        # 오른쪽 누적
        right_set.add(topping[n - i - 1])
        right_cnt[n - i - 1] = len(right_set)
    
    
    # 공평한 지점 찾기
    for i in range(n - 1):
        if left_cnt[i] == right_cnt[i + 1]:
            answer += 1
    
    return answer
