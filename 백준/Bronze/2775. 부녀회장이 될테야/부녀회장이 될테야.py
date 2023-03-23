n=int(input())

for T in range(n):
     k=int(input())           # 층
     n=int(input())           # 호
     room=list(range(1,n+1))
     
     nextRoom=room[:]         # 얕은 복사
     for _ in range(k):       # 층수만큼 반복
          for i in range(n):  # 합을 구하기 위해 반복
               nextRoom[i]=sum(room[0:i+1])
          room=nextRoom[:]
          
     print(room[n-1])