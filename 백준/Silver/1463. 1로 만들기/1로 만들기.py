import sys
input=sys.stdin.readline

n=int(input())
num=[0,0,1,1]
for i in range(4,n+1):
    if i%6==0:      num.append(min(num[i-1],num[i//2],num[i//3])+1)
    elif i%3==0:    num.append(min(num[i-1],num[i//3])+1)
    elif i%2==0:    num.append(min(num[i-1],num[i//2])+1)
    else:           num.append(num[i-1]+1)
print(num[n])