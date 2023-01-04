import sys
input=sys.stdin.readline

for i in range(3):
    result=0
    n=int(input())
    for j in range(n):
        result+=int(input())
    if result>0:
        print('+')
    elif result==0:
        print('0')
    elif result<0:
        print('-')