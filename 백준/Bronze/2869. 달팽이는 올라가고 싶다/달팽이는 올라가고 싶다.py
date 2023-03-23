a,b,v=map(int,input().split())

# v를 (a-b)*n+a로 만들어 준 후 계산하자

if (v-a)%(a-b)!=0:
     v+=(a-b)-((v-a)%(a-b))
     
print((v-a)//(a-b)+1)