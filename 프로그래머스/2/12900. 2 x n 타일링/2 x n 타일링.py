def solution(n):
    
    s1, s2 = 1, 2
    
    for i in range(n - 2):
        s1, s2 = s2, s1 + s2

    return s2 % 1000000007
