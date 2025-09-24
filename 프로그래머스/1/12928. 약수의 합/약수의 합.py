def solution(n):
    
    answer = 0
    n_sqrt = n ** 0.5
    
    for i in range(1, int(n_sqrt) + 1):
        if n % i == 0:
            answer += i
            answer += n // i
            
    if n_sqrt == int(n_sqrt):
        answer -= int(n_sqrt)
    
    return answer