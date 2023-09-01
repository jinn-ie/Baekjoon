import sys
input=sys.stdin.readline

def dfs(first,computers,networks):
    if computers[first-1]==False:
        computers[first-1]=True
        for network in networks:
            if network[0]==first:
                dfs(network[1],computers,networks)
                del network
            elif network[1]==first:
                dfs(network[0],computers,networks)
                del network
        

def main():
    computer=int(input())
    n=int(input())
    
    computers=[False]*computer  # 바이러스 감염 여부 체크리스트
    networks=[]
    
    for i in range(n):
        networks.append(list(map(int,input().split())))
        
    dfs(1,computers,networks)
    
    print(computers.count(True)-1)
    
main()