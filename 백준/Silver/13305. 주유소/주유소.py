import sys
input = sys.stdin.readline

n = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

res = 0
min_price = price[0]

for i in range(n - 1):
    if price[i] < min_price:
        min_price = price[i]

    res += min_price * km[i]

print(res)