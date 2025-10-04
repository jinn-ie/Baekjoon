def solution(n):
    
    MOD = 1000000007
    n1, n2 = 1, 2
    
    for _ in range(n - 2):
        n1, n2 = n2, (n1 + n2) % MOD 

    return n2
