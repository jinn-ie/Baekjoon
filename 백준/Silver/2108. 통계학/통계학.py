from collections import Counter
import sys
input=sys.stdin.readline

n=int(input())
nums=[]
for _ in range(n):
     nums.append(int(input()))

nums.sort()

# 산술평균 : sum 사용    
print(round(sum(nums)/n))

# 중앙값 : 정렬된 리스트 indexing
print(nums[n//2])

# 최빈값 : counter 생성 후 앞쪽 index 탐색
c=Counter(nums)
freq=0

for k,v in c.items():
     if freq<v:               # 초기 설정 또는 새로운 최빈값이면
          freqKeyList=[k]
          freq=v
     elif freq==v:            # 같은 최빈값이면
          freqKeyList.append(k)
          
freqKeyList.sort()

if len(freqKeyList)==1: print(freqKeyList[0])
else: print(freqKeyList[1])

# 범위 : 최대, 최소 indexing
print(nums[n-1]-nums[0])