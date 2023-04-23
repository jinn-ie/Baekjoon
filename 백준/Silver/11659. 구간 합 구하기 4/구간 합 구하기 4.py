import sys
input=sys.stdin.readline

n,m=map(int,input().split())
num_list=list(map(int,input().split()))

sum_list=[0]
prev=0
for i in range(n):
    sum_list.append(prev+num_list[i])
    prev+=num_list[i]

for _ in range(m):
    start,end=map(int,input().split())
    print(sum_list[end]-sum_list[start-1])