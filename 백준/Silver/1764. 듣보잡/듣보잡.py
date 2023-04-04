import sys
from collections import Counter
input=sys.stdin.readline

people=[]
n,m=map(int,input().split())
for _ in range(n+m):
    people.append(input().rstrip())
    
c=Counter(people)

result=[]
for person in c:
    if c[person]==2:
        result.append(person)
        
result.sort()        
print(len(result))
for person in result:
    print(person)