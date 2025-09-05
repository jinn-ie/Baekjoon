def solution(board, moves):
    
    stack = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):             # 위에서부터 인형이 존재할 때까지 탐색
            cur = board[i][move - 1]
            if cur != 0:                        # 맨 위의 인형 발견
                board[i][move - 1] = 0
                if stack and stack[-1] == cur:  # 같은 모양일 때 터뜨림
                    stack.pop()
                    answer += 2
                else:                           # 다른 모양일 때 바구니에 추가
                    stack.append(cur)
                break
    
    return answer