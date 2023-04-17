import sys
input=sys.stdin.readline

minus=list(input().rstrip().split('-'))

for i in range(len(minus)):
    plus=list(map(int,minus[i].split('+')))
    minus[i]=sum(plus)

res=minus[0]
for i in range(1,len(minus)): res-=minus[i]
print(res)