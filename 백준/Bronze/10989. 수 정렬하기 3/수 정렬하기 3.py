import sys
input=sys.stdin.readline
nums=[0 for i in range(10000)]
n=int(input())

for _ in range(n):
     nums[int(input())-1]+=1
               
for i in range(10000):
     if nums[i]!=0:
          for _ in range(nums[i]):
               print(i+1)