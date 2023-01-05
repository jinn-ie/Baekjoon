n,k=map(int,input().split())
i=k-1
people=list(range(1,n+1))
print('<',end='')

while (len(people)!=1):
    while (i>=len(people)):
        i=i-len(people)
    print(people[i],end=', ')
    del people[i]
    i+=k-1
    
print(str(people[0])+'>')