import sys
input=sys.stdin.readline

def smaller(paper,area):
    res=[]
    n=len(paper)
    if area==0:
        for i in range(0,n//2):
            res.append(paper[i][0:n//2])
    elif area==1:
        for i in range(0,n//2):
            res.append(paper[i][n//2:n])
    elif area==2:
        for i in range(n//2,n):
            res.append(paper[i][0:n//2])
    elif area==3:
        for i in range(n//2,n):
            res.append(paper[i][n//2:n])
    return res

def add(paper):
    res,n=0,len(paper)
    for i in range(n):
        for j in range(n):
            res+=paper[i][j]
    return res
    
def cut(paper):
    if add(paper)==len(paper)**2:   return [0,1]
    elif add(paper)==0:             return [1,0]
    else:
        a0=cut(smaller(paper,0))
        a1=cut(smaller(paper,1))
        a2=cut(smaller(paper,2))
        a3=cut(smaller(paper,3))
        return [a0[0]+a1[0]+a2[0]+a3[0],a0[1]+a1[1]+a2[1]+a3[1]]

def main():
    paper=[]
    n=int(input())
    for _ in range(n): paper.append(list(map(int,input().split())))

    print(cut(paper)[0])
    print(cut(paper)[1])
    
main()