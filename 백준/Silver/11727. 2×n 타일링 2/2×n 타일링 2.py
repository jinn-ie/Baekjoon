import sys, math
input = sys.stdin.readline

n=int(input())

first,second=1,1
for i in range(n-1):
    first,second=second,first*2+second
    
print(second%10007)