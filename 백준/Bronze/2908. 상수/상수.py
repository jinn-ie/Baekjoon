import sys
input=sys.stdin.readline

a,b=input().split()
a=int("".join(reversed(a)))
b=int("".join(reversed(b)))

print(a if a>b else b)
