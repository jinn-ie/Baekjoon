num_list=list(map(int,input().split()))
result=0
for num in num_list:
    result+=num**2
result%=10
print(result)