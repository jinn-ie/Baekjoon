def solution(sequence, k):
    N = len(sequence)
    left, right = 0, 0
    current_sum = sequence[0]
    answer = []

    while left < N and right < N:
        if current_sum == k:
            answer.append([left, right])
            current_sum -= sequence[left]
            left += 1
        elif current_sum < k:
            right += 1
            if right < N:
                current_sum += sequence[right]
        else:  # current_sum > k
            current_sum -= sequence[left]
            left += 1

    # 가장 짧은 구간(길이 최소) → 시작 인덱스가 작은 순으로
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0] if answer else []
