import sys
from collections import deque
input = sys.stdin.readline

N=int(input().rstrip())
com=[[] for _ in range(N)]
C=int(input().rstrip())

for i in range(C):
    a,b=map(int,input().split())
    com[a-1].append(b-1)
    com[b-1].append(a-1)
d = deque()
visited=[False for _ in range(N)]
d.append(0)
while d:
    now=d.popleft()
    for i in com[now]:
        if not visited[i]:
            d.append(i)
            visited[i]=True

res=0
for i in visited[1:]:
    if i==1:
        res+=1
print(res)