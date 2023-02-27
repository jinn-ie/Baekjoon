n=int(input())
nums=[]

for i in range(n):
     num=int(input())
     
     if num==0:
          del nums[-1]
     else:
          nums.append(num)
          
print(sum(nums))