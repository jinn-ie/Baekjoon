n=int(input())
wdict={}

for i in range(n):
    word=input()
    wdict[word]=len(word)
    
wdict=sorted(wdict.items())
wdict=sorted(wdict,key=lambda item:item[1])
    
for word in wdict:
    print(word[0])