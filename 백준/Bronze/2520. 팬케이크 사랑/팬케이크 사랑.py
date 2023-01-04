n=int(input())

for i in range(n):
    input()
    milk,yolk,sugar,salt,flour=map(float,input().split())
    banana,straw,choco,walnut=map(int,input().split())
    
    cake=[milk/8,yolk/8,sugar/4,salt,flour/9]
    n_cake=int(min(cake)*16)
    
    ingredient=[banana,straw//30,choco//25,walnut//10]
    n_ingr=sum(ingredient)
    
    if (n_cake>n_ingr): print(n_ingr)
    else: print(n_cake)