from collections import deque

def bfs(n,m):
    q = deque()
    q.append(n)
    visited=[0 for i in range(100001)]
    while q:
        now=q.popleft()
        if now==m:
            return visited[now]
        
        for dn in [now-1,now+1,now*2]:
            if 0<=dn<=100000 and not visited[dn]:
                visited[dn]=visited[now]+1
                q.append(dn)
    
N,M=map(int,input().split())
print(bfs(N,M))