judge=[]

n=int(input())

for i in range(n):
    person=list(input().split())
    judge.append(person)

s_judge=sorted(judge,key=lambda x:int(x[0]))

for age,name in s_judge:
    print(age,name)