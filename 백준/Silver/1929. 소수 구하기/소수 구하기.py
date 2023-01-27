m,n=map(int,input().split())
num_list=list(range(m,n+1))
res=[]

i=0
for num in num_list:
    if (num==1):
        pass
    else:
        for i in range(2,int(num**0.5+1)):
            if (num%i==0):
                break
        else: res.append(num)
    
for num in res:
    print(num)