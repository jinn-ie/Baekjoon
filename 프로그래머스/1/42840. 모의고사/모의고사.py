def solution(answers):
    
    answer = []
    
    score = [0, 0, 0]
    
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    for i in range(len(answers)):
        if answers[i] == one[i]:
            score[0] += 1
        if answers[i] == two[i]:
            score[1] += 1
        if answers[i] == three[i]:
            score[2] += 1
    
    max_score = max(score)
    
    for i in range(3):
        if score[i] == max_score:
            answer.append(i + 1)
    
    return answer