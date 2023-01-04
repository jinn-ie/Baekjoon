def gcd(a,b):
    if (b==0):
        return(a)
    else:
        return gcd(b,a%b)
    
def main():
    a,b=map(int,input().split())
    if (a<b):
        a,b=b,a        # python swap
        
    g=gcd(a,b)
    print(g)
    print(g*(a//g)*(b//g))
    
main()