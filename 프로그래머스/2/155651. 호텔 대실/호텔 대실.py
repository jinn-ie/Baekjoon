def time_to_int(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(book_time):
    answer = 0
    book_time.sort()
        
    rooms = []      # 종료 시간 배열
    
    for b in book_time:
        if not rooms: rooms.append(b[1])
        
        else:
            for r in range(len(rooms)):
                # 종료 + 청소시간보다 시작 시간이 늦으면
                if time_to_int(b[0]) >= time_to_int(rooms[r]) + 10:     
                    rooms[r] = b[1]
                    break
            else:
                rooms.append(b[1])
        rooms.sort()
            
    
    return len(rooms)