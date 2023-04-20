import sys
input=sys.stdin.readline

n=int(input())
res=0
num=int(input())
for _ in range(n):
    res+=num%10
    num//=10
print(res)