import sys, math
input = sys.stdin.readline

meetings=[]
n=int(input())
for _ in range(n):
    meetings.append(list(map(int,input().split())))
    
meetings.sort(key=lambda x:(x[1],x[0]))

start,end=meetings[0][0],meetings[0][1]
res=1
for i in range(1,len(meetings)):
    if end<=meetings[i][0]:
        res+=1
        end=meetings[i][1]
 
print(res)