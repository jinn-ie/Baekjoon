def solution(mats, park):
    answer = []
    
    width, length = len(park[0]), len(park)
    
    for i in range(length):
        for j in range(width):
            if park[i][j] == "-1":
                mat = 1
                while i+mat < length and j+mat < width and all(
                        cell == "-1" for row in park[i:i+mat+1] for cell in row[j:j+mat+1]):
                    mat += 1
                answer.append(mat)
                
    answer = sorted(list(set(answer)), reverse=True)
    
    for m in sorted(mats, reverse=True):
        if m in answer: return m
    else:               return -1