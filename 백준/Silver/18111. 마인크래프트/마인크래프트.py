import sys
input=sys.stdin.readline

n,m,inventory=map(int,input().split())
ground=[]
for _ in range(n):
     ground.append(list(map(int,input().split())))
     
minHeight=min(map(min,ground))
maxHeight=max(map(max,ground))

if maxHeight>256: maxHeight=256

timeList=[99999999 for i in range(maxHeight-minHeight+1)]
for HEIGHT in range(minHeight,maxHeight+1):
     time=0
     _inventory=inventory
     addBlock,removeBlock=0,0
     for i in range(n):
          for j in range(m):
               if ground[i][j]>HEIGHT:       # 깎기
                    removeBlock+=ground[i][j]-HEIGHT    
               elif ground[i][j]<HEIGHT:       # 쌓기
                    addBlock+=HEIGHT-ground[i][j]
     _inventory=inventory+removeBlock-addBlock
     if _inventory<0: break
     time=removeBlock*2+addBlock
     timeList[HEIGHT-minHeight]=time
     
timeList.reverse()
print(min(timeList),maxHeight-timeList.index(min(timeList)))