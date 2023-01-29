k,n=map(int,input().split())
lans=[]

for i in range(k):
     lans.append(int(input()))

res=0
start=0
end=max(lans)       # 최대길이로 기준잡아야함!

while(start!=end or res<n):
     res=0
     length=(end+start+1)//2
     for lan in lans:
          res+=lan//length
     if res<n:
          end=(start+end)//2
     elif res>=n:
          start=(start+end+1)//2

print(length)