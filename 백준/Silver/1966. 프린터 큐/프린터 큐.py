n=int(input())

for i in range(n):
     n,m=map(int,input().split())
     queue=list(map(int,input().split()))
     
     while(len(queue)!=0):
          if max(queue)==queue[0]:      # 뽑아야할때
               if m==0:                 # 해당하면 개수 출력
                    print(n-len(queue)+1)
                    break
               del queue[0]
          else:                         # 뒤로넣어야할때
               if m==0:                 # 해당하면
                    m+=len(queue)       # 인덱스는 길이만큼 증가
               queue.append(queue[0])
               del queue[0]
          m-=1