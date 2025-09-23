def solution(answers):
    
    answer = []
    score = [0, 0, 0]
    
    # 배열 연장 (최대 10,000문제)
    p1 = [1, 2, 3, 4, 5] * 2000
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    # 사람별 맞힌 문제 개수 체크
    for i in range(len(answers)):
        if answers[i] == p1[i]: score[0] += 1
        if answers[i] == p2[i]: score[1] += 1
        if answers[i] == p3[i]: score[2] += 1
    
    for i in range(3):
        if score[i] == max(score):  # 최고점이면
            answer.append(i + 1)    # 정답 배열에 추가
    
    return answer