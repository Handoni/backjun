import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())

array =[[] for _ in range(N)]
for _ in range(M):
    u,v=map(int,input().split())
    array[u-1].append(v-1)
    array[v-1].append(u-1)
visited=[0 for _ in range(N)]

def bfs(s):
    d=deque()
    d.append(s)
    visited[s]=1
    while d:
        now=d.popleft()
        for i in array[now]:
            if not visited[i]:
                d.append(i)
                visited[i]=1

bfs(0)
res=1
while True:
    for i in range(N):
        if visited[i]==0:
            bfs(i)
            res+=1
            continue
    break
print(res)