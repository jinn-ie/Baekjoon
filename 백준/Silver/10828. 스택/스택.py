import sys
input=sys.stdin.readline

stack=[]
n=int(input())

for i in range(n):
    command=input().rstrip()
    if command.startswith('push'):
        c,n=command.split()
        stack.append(n)
    elif command=='pop':
        if not stack:       # if list is empty
            print(-1)
        else: 
            print(stack[-1])
            del stack[-1]
    elif command=='size':
        print(len(stack))
    elif command=='empty':
        if not stack: print(1)
        else: print(0)
    elif command=='top':
        if not stack: print(-1)
        else: print(stack[-1])