import heapq,sys
input=sys.stdin.readline

n=int(input())
maxHeap=[]
for _ in range(n):
    x=int(input())
    if x==0:
        if not maxHeap: print(0)
        else:
            print(maxHeap[0])
            heapq.heappop(maxHeap)
    else:
        heapq.heappush(maxHeap,x)