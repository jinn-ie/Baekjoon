import sys
input=sys.stdin.readline

n=int(input())

first,second=0,1
for i in range(n):
    first,second=second,first+second
print(second%10007)