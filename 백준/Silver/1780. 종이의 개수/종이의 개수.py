import sys
input=sys.stdin.readline

paper=[]
res=[0,0,0]
    
def cut(n,col,row):
    for i in range(row,row+n):
        for j in range(col,col+n-1):
            if paper[i][j]!=paper[i][j+1]:
                n//=3
                return cut(n,col,row)+cut(n,col+n,row)+cut(n,col+n*2,row)+cut(n,col,row+n)+cut(n,col+n,row+n)+cut(n,col+n*2,row+n)+cut(n,col,row+n*2)+cut(n,col+n,row+n*2)+cut(n,col+n*2,row+n*2)
    else:
        for i in range(row,row+n-1):
            if paper[i][col]!=paper[i+1][col]:
                n//=3
                return cut(n,col,row)+cut(n,col+n,row)+cut(n,col+n*2,row)+cut(n,col,row+n)+cut(n,col+n,row+n)+cut(n,col+n*2,row+n)+cut(n,col,row+n*2)+cut(n,col+n,row+n*2)+cut(n,col+n*2,row+n*2)
        else:
            res[paper[row][col]+1]+=1
            return res
        
def main():
    n=int(input())
    for _ in range(n): paper.append(list(map(int,input().split())))
    cut(n,0,0)
    
    for r in res:
        print(r)
    
main()