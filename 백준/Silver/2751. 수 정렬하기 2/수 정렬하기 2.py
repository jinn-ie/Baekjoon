import sys
input=sys.stdin.readline

nlist=[]
n=int(input())

for i in range(n):
    num=int(input())
    nlist.append(num)

nlist.sort()
for num in nlist:
    print(num)