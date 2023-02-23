import sys
input=sys.stdin.readline

n=int(input())
stack=[]
stackNum=1
result=''

for i in range(n):
     num=int(input())
     if stackNum<=num:
          while(stackNum<=num):
               stack.append(stackNum)
               result+='+\n'
               stackNum+=1
     elif stack[-1]!=num:
               result='NO'
               break
          
     del stack[-1]
     result+='-\n'
          
print(result.rstrip())