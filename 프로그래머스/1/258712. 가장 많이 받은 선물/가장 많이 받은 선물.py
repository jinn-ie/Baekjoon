def solution(friends, gifts):
    answer = 0
    N = len(friends)
    f_dict = {friend: idx for idx, friend in enumerate(friends)}
    
    grid = [[0] * N for _ in range(N)]
    
    for gift in gifts:
        give, take = gift.split()
        grid[f_dict[give]][f_dict[take]] += 1
    
    gift_count = [0] * N
    
    for i in range(N):
        for j in range(i + 1, N):
            if grid[i][j] > grid[j][i]:     # 준 게 더 많음
                gift_count[i] += 1
            elif grid[i][j] < grid[j][i]:   # 받은 게 더 많음
                gift_count[j] += 1
            else:                           # 서로 주고받은 수 같음
                i_score = sum(grid[i]) - sum(r[i] for r in grid)
                j_score = sum(grid[j]) - sum(r[j] for r in grid)
                if i_score > j_score:
                    gift_count[i] += 1
                elif i_score < j_score:
                    gift_count[j] += 1
    
    return max(gift_count)