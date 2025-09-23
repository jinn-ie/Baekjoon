def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(0, len(citations)):
        if citations[i] >= len(citations) - i:
            answer = len(citations) - i
            break
            
    return answer