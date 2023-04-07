import sys
input=sys.stdin.readline

n=int(input())

first,second=0,1
for i in range(n):
    first,second=second,first+second
print(second%10007)

# 팩토리얼 : 무식한 방법.. 수가 너무 커져서 다른 값이 나와버림