import sys
input=sys.stdin.readline

n=int(input())

xy=[]
for i in range(n):
    xy.append(list(map(int,input().rstrip().split())))

xy.sort()    
for num in xy:
    print(*num)