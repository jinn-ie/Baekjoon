n = int(input())

for i in range(n - 1):
    print(' ' * i, end='')
    print('*' * ((n - i) * 2 - 1))

for i in range(n - 1, -1, -1):
    print(' ' * i, end='')
    print('*' * ((n - i) * 2 - 1))  