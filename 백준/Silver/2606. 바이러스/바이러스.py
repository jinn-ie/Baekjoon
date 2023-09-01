import sys
input=sys.stdin.readline

computers=[]
networks=[]

def dfs(first):                                 # dfs-재귀로 구현
    if computers[first-1]==False:
        computers[first-1]=True
        for network in networks:                # 연결 탐색
            if network[0]==first:
                dfs(network[1])
                del network                     # 계산이 끝나면 삭제
            elif network[1]==first:             # 역연결도 고려
                dfs(network[0])
                del network

def main():
    c=int(input())
    n=int(input())
    for _ in range(c):  computers.append(False)  # 바이러스 감염 여부 체크리스트
    for _ in range(n):  networks.append(list(map(int,input().split())))
        
    dfs(1)
    
    print(computers.count(True)-1)
    
main()