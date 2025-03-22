import sys
input = sys.stdin.readline

n = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()

res = 0

while price:
    idx = price.index(min(price))
    for i in range(len(price) - 1, idx - 1, -1):
        res += km[i] * price[idx]
        km.pop()
        price.pop()

print(res)