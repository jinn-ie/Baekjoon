def solution(array, commands):
    answer = []
    for command in commands:
        s, e, i = command
        sliced_array = array[s-1:e]
        sliced_array.sort()
        answer.append(sliced_array[i-1])
    return answer