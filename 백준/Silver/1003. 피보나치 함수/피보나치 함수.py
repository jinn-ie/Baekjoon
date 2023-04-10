import sys
input=sys.stdin.readline

T=int(input())
for T in range(T):
    n=int(input())
    
    fzero,fone=1,0
    szero,sone=0,1
    
    if n==0: print(fzero,fone)
    elif n==1: print(szero,sone)
    else:
        for _ in range(1,n):
            fzero,fone,szero,sone=szero,sone,fzero+szero,fone+sone
        print(szero,sone)