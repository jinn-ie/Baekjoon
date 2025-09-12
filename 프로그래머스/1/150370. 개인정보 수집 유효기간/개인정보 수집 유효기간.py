def solution(today, terms, privacies):
    answer = []
    
    today = int(today.replace(".", ""))
    
    term_d = {}
    for term in terms:
        t, m = term.split()
        term_d[t] = int(m)
    
    for i in range(len(privacies)):
        date, t = privacies[i].split()
        date = int(date.replace(".",""))
        
        y = date // 10000
        md = date % 10000
        
        md += term_d[t] * 100
        while md >= 1300:
            md -= 1200
            y += 1
        date = y * 10000 + md -1

        if date < today: answer.append(i + 1)
    
    return answer