def solution(wallpaper):
    answer = []
    
    for i in range(len(wallpaper)):         # 전체 순회
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':      # 파일이 있을 때만
                if not answer:              # 첫 파일
                    answer.extend([i, j, i + 1, j + 1])
                else:                       # 기존 값과 비교해서 갱신
                    answer[0] = min(answer[0], i)
                    answer[1] = min(answer[1], j)
                    answer[2] = max(answer[2], i + 1)
                    answer[3] = max(answer[3], j + 1)
                
    return answer