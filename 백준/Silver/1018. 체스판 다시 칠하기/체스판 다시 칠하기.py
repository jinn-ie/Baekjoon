y,x=map(int,input().split())

chessboard=[]
for i in range(y):
    string=input()
    chessboard.append(string)

cntlist=[]
for sj in range(y-7):
    for si in range(x-7):
        cnt=0
        start=chessboard[sj][si]
        startindex=(si+sj)%2
        for j in range(sj,sj+8):
            for i in range(si,si+8):
                if ((i+j)%2==startindex):
                    if (chessboard[j][i]!=start): cnt+=1
                else:
                    if (chessboard[j][i]==start): cnt+=1
                    
        if (cnt>32): cnt=64-cnt
        cntlist.append(cnt)
        
print(min(cntlist))