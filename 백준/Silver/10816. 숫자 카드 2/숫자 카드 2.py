from collections import Counter
import sys
input=sys.stdin.readline

input()
card_list=list(input().split())
input()
num_list=list(input().split())

                        # 시간초과 해결방안
c=Counter(card_list)    # 요소,빈도수 쌍의 딕셔너리 생성

for num in num_list:
    if num in c:
        print(c[num],end=' ')
    else:
        print(0,end=' ')