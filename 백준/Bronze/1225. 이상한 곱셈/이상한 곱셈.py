import sys
input=sys.stdin.readline

ra,rb=0,0
a,b=input().rstrip().split()

for i in a:
    ra+=int(i)
for i in b:
    rb+=int(i)
    
print(ra*rb)