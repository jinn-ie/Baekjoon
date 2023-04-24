import sys
input=sys.stdin.readline

def slicing(video,area):
    res=[]
    n=len(video)
    if area==0:
        for i in range(n//2):
            res.append(video[i][0:n//2])
    elif area==1:
        for i in range(n//2):
            res.append(video[i][n//2:n])
    elif area==2:
        for i in range(n//2,n):
            res.append(video[i][0:n//2])
    elif area==3:
        for i in range(n//2,n):
            res.append(video[i][n//2:n])
    return res
    
def quadtree(video):
    n=len(video)
    for i in range(n**2-1):
        if video[i//n][i%n]!=video[(i+1)//n][(i+1)%n]:
            return "("+quadtree(slicing(video,0))+quadtree(slicing(video,1))+quadtree(slicing(video,2))+quadtree(slicing(video,3))+")"
            break
    else:
        return video[0][0]

def main():
    n=int(input())
    video=[]
    for _ in range(n):
        video.append(input().rstrip())
    print(quadtree(video))
        
main()