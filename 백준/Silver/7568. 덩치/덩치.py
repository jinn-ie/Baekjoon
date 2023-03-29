import sys
input=sys.stdin.readline

people=[]
n=int(input())
for _ in range(n):
     people.append(tuple(map(int,input().split())))
     
sizes=[]
for person in people:
     size=1
     for comPerson in people:
          if comPerson[0]>person[0] and comPerson[1]>person[1]:
               size+=1
     sizes.append(size)
     
print(*sizes)