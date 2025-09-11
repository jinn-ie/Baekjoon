def solution(schedules, timelogs, startday):
    answer = 0
    
    weekend = [(6 - startday) % 7, (7 - startday) % 7]
    
    for i in range(len(schedules)):
        schedule = schedules[i] + 10    # 출석 인증 시각 설정
        if schedule % 100 >= 60:
            schedule -= 60
            schedule += 100
        
        for t in range(7):
            if t in weekend:                    continue    # 주말
            elif timelogs[i][t] <= schedule:    continue    # 출석 성공
            else:                               break       # 출석 실패
        else: answer += 1
            
    
    return answer