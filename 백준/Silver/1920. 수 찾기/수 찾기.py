def binary(n_list,num,start,end):
    # in 사용하면 순차 탐색 -> 시간초과
    if (start>end):
        return False
    
    curr=(start+end)//2
    
    if (num<n_list[curr]):
        return binary(n_list,num,start,curr-1)
    elif (num==n_list[curr]):
        return True
    elif (num>n_list[curr]):
        return binary(n_list,num,curr+1,end)
  
    
def main():
    n=int(input())
    n_list=list(map(int,input().split()))
    m=int(input())
    m_list=list(map(int,input().split()))
    
    n_list.sort()
    for i in range(m):
        if(binary(n_list,m_list[i],0,len(n_list)-1)):
            print(1)
        else:
            print(0)
            
main()