import heapq,sys
input=sys.stdin.readline

n=int(input())
minHeap=[]
for _ in range(n):
    x=int(input())
    if x==0:
        if not minHeap: print(0)
        else:
            print(minHeap[0])
            heapq.heappop(minHeap)
    else:
        heapq.heappush(minHeap,x)