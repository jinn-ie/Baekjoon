import heapq                                                     # 최소 힙만 지원
import sys
input=sys.stdin.readline

testcase=int(input())
for T in range(testcase):
     maxH,minH=[],[]
     
     n=int(input())
     exists=[False]*n                                            # 동기화 위한 체크리스트
     
     for i in range(n):
          command,num=input().split()
          
          if command=='I':
               heapq.heappush(minH,(int(num),i))                 # 반복문의 횟수 i를 id로 사용
               heapq.heappush(maxH,(int(num)*-1,i))              # 최대 힙 구현법
               exists[i]=True
               
          elif command=='D':
               if num=='1':
                    while (maxH and not exists[maxH[0][1]]):     # 동기화 후 (delete시 계속 해주어야 함! : 테케1번)
                         heapq.heappop(maxH)
                    if maxH:                                     # 남아있으면 delete
                         exists[maxH[0][1]]=False
                         heapq.heappop(maxH)
               elif num=='-1':
                    while (minH and not exists[minH[0][1]]):
                         heapq.heappop(minH)
                    if minH:
                         exists[minH[0][1]]=False
                         heapq.heappop(minH)
     
     # 각각 최대, 최소 전까지만 동기화
     while (maxH and not exists[maxH[0][1]]):
          heapq.heappop(maxH)
     while (minH and not exists[minH[0][1]]):
          heapq.heappop(minH)
     
     if not maxH or not minH:
          print('EMPTY')
     else:
          print(-maxH[0][0],minH[0][0])