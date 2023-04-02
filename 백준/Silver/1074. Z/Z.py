def Z(n,r,c,start):
     if n>1:
          divisor=2**(n-1)
          return Z(n-1, r%divisor, c%divisor, start+(r//divisor*2+c//divisor)*(divisor**2))
     else:
          return start+r*2+c
     
def main():
     n,r,c=map(int,input().split())
     print(Z(n,r,c,0))
     
main()