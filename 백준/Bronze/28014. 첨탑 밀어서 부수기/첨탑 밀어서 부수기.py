import sys
input=sys.stdin.readline

n=int(input())
tops=list(map(int,input().split()))

before,res=0,0
for top in tops:
    if top>=before: res+=1
    before=top
    
print(res)