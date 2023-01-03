pitch=list(map(int,input().split()))

if (pitch[0]==1):
    check='ascending'
    for i in range(1,7):                    # feedback: for문 없이 sorted 이용하면 간단함
        if (pitch[i]+1!=pitch[i+1]):
            check='mixed'
            break
elif (pitch[0]==8):
    check='descending'
    for i in range(1,7):
        if (pitch[i]-1!=pitch[i+1]):
            check='mixed'
            break    
else: check='mixed'

print(check)
