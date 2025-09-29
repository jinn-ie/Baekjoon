def solution(board):
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    len_x, len_y = len(board[0]), len(board)
    distance = [[99999999] * len_x for _ in range(len_y)]
    
    for i in range(len_y):
        if 'R' in board[i]: r = [i, board[i].index('R')]
        if 'G' in board[i]: g = [i, board[i].index('G')]
            
    queue = [[r[0], r[1]]]
    distance[r[0]][r[1]] = 0
    
    while queue:
        yy, xx = queue[0][0], queue[0][1]
        del queue[0]

        for i in range(4):
            y, x = yy, xx
            dis = distance[y][x]
            
            while True:
                if x + dx[i] >= len_x or x + dx[i] < 0: break
                if y + dy[i] >= len_y or y + dy[i] < 0: break
                if board[y + dy[i]][x + dx[i]] == 'D': break
                
                y += dy[i]
                x += dx[i]
                
            if distance[y][x] > dis + 1:
                distance[y][x] = dis + 1
                queue.append([y, x])
                    
                
    answer = distance[g[0]][g[1]]
    if answer == 99999999: answer = -1
    return answer