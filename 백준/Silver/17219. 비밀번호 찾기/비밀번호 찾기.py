import sys
input=sys.stdin.readline

n,m=map(int,input().split())

passList={}
for _ in range(n):
     site,password=input().split()
     passList[site]=password
     
for _ in range(m):
     target=input().rstrip()
     print(passList[target])