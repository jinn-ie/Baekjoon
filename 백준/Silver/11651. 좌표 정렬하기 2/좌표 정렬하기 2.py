n=int(input())
dots=[]

for i in range(n):
     dots.append(list(map(int,input().split())))

dots.sort(key=lambda x: (x[1],x[0]))    # 두가지 조건 표현
     
for dot in dots:
     print(*dot)