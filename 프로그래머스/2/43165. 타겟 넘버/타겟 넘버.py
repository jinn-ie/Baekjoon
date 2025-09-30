def solution(numbers, target):
    answer = 0
    stack = [[0, numbers[0]], [0, -numbers[0]]]
    
    # DFS
    while stack:
        idx, num = stack.pop()
        if idx == len(numbers) - 1:         # 마지막 수까지 계산했을 때
            if num == target: answer += 1   # 타겟 넘버면 answer++
            continue
        
        stack.append([idx + 1, num + numbers[idx + 1]]) # 스택에 idx째까지의 연산 저장
        stack.append([idx + 1, num - numbers[idx + 1]])    
    
    return answer