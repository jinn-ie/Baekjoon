n,m=map(int,input().split())
cards=list(map(int,input().split()))

cards.sort(reverse=True)      # 내림차순정렬

result=[]

for i in range(n-2):
     for j in range(i+1,n-1):
          for k in range(j+1,n):
               if (cards[i]+cards[j]+cards[k]<=m):
                    result.append(cards[i]+cards[j]+cards[k])
                    
print(max(result))