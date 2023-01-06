n=int(input())

for i in range(n):
    stack=[]
    vps='YES'
    string=input()
    for j in range(len(string)):
        if (string[j]=='('):
            stack.append('(')
        elif (string[j]==')'):
            if not stack:
                vps='NO'
                break
            else:
                del stack[-1]
    if stack: vps='NO'
    
    print(vps)