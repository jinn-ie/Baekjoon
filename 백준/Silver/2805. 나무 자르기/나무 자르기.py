import sys
input=sys.stdin.readline

n,m=map(int,input().split())
woods=list(map(int,input().split()))

# 초기설정
low=0
high=max(woods)

# 이분탐색
while(True):
     h=(low+high)//2
     get=0
     for wood in woods:
          if wood-h>0: get+=wood-h
          if get>m: break
     
     if get<m: high=h
     elif get>m: low=h
     else:
          print(h) 
          break
     if low+1==high: 
          if low==h: print(h)
          elif high==h: print(h-1)
          break