from collections import deque
n=int(input())

queue=deque(range(1,n+1))

while(len(queue)>1):
     queue.popleft()     # list는 indexing에서 시간이 걸림
     queue.append(queue[0])
     queue.popleft()
     
print(queue[-1])
