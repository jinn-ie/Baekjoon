n=int(input())
numlist=list(map(int,input().split()))

res=n

for num in numlist:
    if (num==1): res-=1
    else:
        for i in range(2,int(num**0.5)+1):
            if (num%i==0):
                res-=1
                break
            
print(res)