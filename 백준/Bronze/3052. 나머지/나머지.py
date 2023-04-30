import sys
input=sys.stdin.readline
num_list=[]

for i in range(10):
    num_list.append(int(input())%42)
    
num_list=set(num_list)
print(len(num_list))