import sys
input=sys.stdin.readline

n=int(input())
if n==0: print(0)
else:
    levels=[]
    for i in range(n): levels.append(int(input()))
    levels.sort()

    del_num=round(n*0.15+0.000001)
    del_list=levels[del_num:n-del_num]
    print(round(sum(del_list)/(n-2*del_num)+0.000001))