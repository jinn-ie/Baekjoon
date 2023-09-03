import sys
input = sys.stdin.readline

num_list = [0] * 10
result = 1

for _ in range(3):          result*=int(input())
for char in str(result):    num_list[int(char)]+=1
for i in range(10):         print(num_list[i])