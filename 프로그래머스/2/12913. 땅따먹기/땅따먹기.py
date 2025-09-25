def solution(land):

    prev = land[0]
    
    for i in range(1, len(land)):
        
        cur = []
        
        for j in range(4):
            copy_prev = prev[:]
            
            del copy_prev[j]
            cur.append(max(copy_prev) + land[i][j])
            
        prev = cur

    return max(cur)