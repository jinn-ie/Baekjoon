import sys
input=sys.stdin.readline

n=int(input())
numList=list(map(int,input().split()))

order={}
sortedNumList=sorted(set(numList))
for i in range(len(sortedNumList)):
    order[sortedNumList[i]]=i

for num in numList:
    print(order[num],end=' ')