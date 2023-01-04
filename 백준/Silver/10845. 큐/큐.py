import sys
input=sys.stdin.readline
        
que=[]
n=int(input())

for i in range(n):
    command=input().rstrip()
    if command.startswith('push'):
        c,num=command.split()
        que.append(num)
    elif command=='pop':
        if not que:
            print(-1)
        else:
            print(que[0])
            del que[0]
    elif command=='size':
        print(len(que))
    elif command=='empty':
        if not que:
            print(1)
        else:
            print(0)
    elif command=='front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif command=='back':
        if not que:
            print(-1)
        else:
            print(que[-1])