import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    n=int(input())
    first,second,third=1,2,4
    if n<4:
        if n==1: print(first)
        elif n==2: print(second)
        elif n==3: print(third)
    else:
        for _ in range(n-3):
            first,second,third=second,third,first+second+third
        print(third)