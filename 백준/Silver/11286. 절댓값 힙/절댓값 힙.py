import sys,heapq
input=sys.stdin.readline

plusHeap,minusHeap=[],[]
n=int(input())
for _ in range(n):
    x=int(input())
    if x==0:
        if not (plusHeap or minusHeap):
            print(0)
        elif not plusHeap:
            print(-minusHeap[0])
            heapq.heappop(minusHeap)
        elif not minusHeap:
            print(plusHeap[0])
            heapq.heappop(plusHeap)
        else:
            if plusHeap[0]<minusHeap[0]:
                print(plusHeap[0])
                heapq.heappop(plusHeap)
            elif minusHeap[0]<=plusHeap[0]:
                print(-minusHeap[0])
                heapq.heappop(minusHeap)
    elif x>0:
        heapq.heappush(plusHeap,x)
    elif x<0:
        heapq.heappush(minusHeap,-x)