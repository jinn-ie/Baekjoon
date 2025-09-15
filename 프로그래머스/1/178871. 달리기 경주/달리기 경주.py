def solution(players, callings):
    
    index = range(len(players))
    
    players_d = dict(zip(players, index))
    ranks_d = dict(zip(index, players))

    for call in callings:
        players_d[call] -= 1        # kai - 1
        
        rank = players_d[call]
        front = ranks_d[rank]       # poe
        
        ranks_d[rank] = call        # 2 = kai
        ranks_d[rank + 1] = front   # 3 = poe
        players_d[front] += 1       # poe + 1
    
    return list(ranks_d.values())