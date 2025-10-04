def solution(ingredient):
    answer = 0
    
    hamburger = [1, 2, 3, 1]
    
    stack = []
    
    for i in ingredient:
        stack.append(i)
        
        if len(stack) >= 4 and stack[-4:] == hamburger:
            del stack[-4:]
            answer += 1
            
    return answer