import sys
input=sys.stdin.readline

n,x=map(int,input().split())
num_list=list(map(int,input().split()))

res=[]

for num in num_list:
    if num<x: res.append(num)
    
print(*res)