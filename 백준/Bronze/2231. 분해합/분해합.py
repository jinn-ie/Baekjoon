n=int(input())

for i in range(1,n+1):
     res=i
     for num in str(i):
          res+=int(num)
     if (res==n):
          print(i)
          break
else:
     print(0)