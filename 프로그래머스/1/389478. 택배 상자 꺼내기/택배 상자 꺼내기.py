def solution(n, w, num):
    answer = 1
    
    step_a = (((num - 1) // w + 1) * w + 1 - num) * 2 - 1
    step_b = w * 2 - step_a
    
    while True:
        if answer % 2 != 0: step = step_a
        else:               step = step_b
        
        if num + step > n: break
        
        num += step
        answer += 1
        
    return answer