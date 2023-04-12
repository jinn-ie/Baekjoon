import sys,heapq
input=sys.stdin.readline

minHeap=[]
n=int(input())
for _ in range(n):
    x=int(input())
    if x==0:
        if not minHeap: print(0)
        else:
            print(-minHeap[0])
            heapq.heappop(minHeap)
    else:
        heapq.heappush(minHeap,-x)