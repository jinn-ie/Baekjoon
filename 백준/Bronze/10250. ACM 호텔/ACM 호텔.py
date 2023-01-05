n=int(input())

for i in range(n):
    h,w,o=map(int, input().split())
    if(o%h==0):
        print(h*100+o//h)
    else: print(o%h*100+o//h+1)