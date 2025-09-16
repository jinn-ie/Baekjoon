def solution(park, routes):
    
    h = len(park)
    w = len(park[0])
    
    for i in range(h):  # S의 위치 찾기
        if 'S' in park[i]:
            x, y = park[i].index('S'), i
            break
            
    for route in routes:
        
        direction, length = route.split()
        length = int(length)
        
        if direction == 'E':
            if x + length < w and not 'X' in park[y][x+1:x+length+1]:
                x += length
        elif direction == 'W':
            if x - length > -1 and not 'X' in park[y][x-length:x]:
                x -= length
        elif direction == 'S':  # y 슬라이싱+in 구문이 안돼서 all로 구현
            if y + length < h and all(park[i][x] != 'X' for i in range(y + 1, y + length + 1)):
                y += length
        elif direction == 'N':
            if y - length > -1 and all(park[i][x] != 'X' for i in range(y - length, y)):
                y -= length
    
    return [y, x]