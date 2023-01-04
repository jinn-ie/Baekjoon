import sys
input=sys.stdin.readline
        
deque=[]
n=int(input())

for i in range(n):
    command=input().rstrip()
    if command.startswith('push_front'):
        c,num=command.split()
        deque.insert(0,num)
    if command.startswith('push_back'):
        c,num=command.split()
        deque.append(num)
    elif command=='pop_front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
            del deque[0]
    elif command=='pop_back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])
            del deque[-1]
    elif command=='size':
        print(len(deque))
    elif command=='empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif command=='front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif command=='back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])