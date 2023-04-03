import sys
input=sys.stdin.readline

s=[]
n=int(input())
for _ in range(n):
    command=input()
    if command.startswith('all'):
        s=list(range(1,21))
    elif command.startswith('empty'):
        s=[]
    else:
        c,num=command.split()
        num=int(num)
        if c=='add':
            if num not in s: s.append(num)
        elif c=='remove':
            if num in s: s.remove(num)
        elif c=='check':
            if num in s: print(1)
            else: print(0)
        elif c=='toggle':
            if num in s: s.remove(num)
            else: s.append(num)