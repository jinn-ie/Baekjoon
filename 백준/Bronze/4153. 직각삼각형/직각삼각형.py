a,b,c=map(int,input().split())

while not (a==b==c==0):
    if (a<=c and b<=c):
        if (a**2+b**2==c**2): print('right')
        else: print('wrong')
    elif (a<=b and c<=b):
        if (a**2+c**2==b**2): print('right')
        else: print('wrong')
    elif (b<=a and c<=a):
        if (b**2+c**2==a**2): print('right')
        else: print('wrong')
    a,b,c=map(int, input().split())