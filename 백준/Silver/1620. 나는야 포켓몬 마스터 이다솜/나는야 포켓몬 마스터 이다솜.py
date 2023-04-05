import sys
input=sys.stdin.readline

pokemonNum={}
pokemonName={}
n,m=map(int,input().split())
for i in range(1,n+1):
    name=input().rstrip()
    pokemonNum[i]=name
    pokemonName[name]=i

for _ in range(m):
    _in=input().rstrip()
    if _in.isdigit():
        print(pokemonNum[int(_in)])
    else:
        print(pokemonName[_in])