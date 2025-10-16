def solution(bandage, health, attacks):
    answer = 0
    before = 0
    t, x, y = bandage
    max_health = health
    
    for attack in attacks:
        sec = attack[0] - before - 1
        
        health = min(max_health, health + sec * x + sec // t * y)
        health -= attack[1]
        before = attack[0]
        
        if health <= 0: return -1
    
    return health