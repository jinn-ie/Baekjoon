n,k=map(int,input().split())
res=1

if (k>n//2): k=n-k
for i in range(k):
    res*=(n-i)/(i+1)
    
print(int(res))