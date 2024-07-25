from collections import deque

def naming(i:int,j:int,d:int=-1):
    if d==-1:
        return str(i)+' '+str(j)
    else:
        return str(i)+' '+str(j)+' '+str(d)
def dename(s:str):
    return map(int,s.split())

N,M=map(int,input().split())

miro = list()
for _ in range(N):
    miro.append(list(input()))
    
q = deque()
visited = list()

n=m=0
d=1
q.append(naming(n,m,d))
visited.append(naming(n,m))
res=1

while True:
    n,m,d=dename(q.popleft())
    
    if n==N-1 and m==M-1:
        print(d)
        break
    if n<N-1:
        if (miro[n+1][m] == '1') and (naming(n+1,m) not in visited):
            q.append(naming(n+1,m,d+1))
            visited.append(naming(n+1,m))
    
    if n>0:
        if (miro[n-1][m] == '1') and (naming(n-1,m) not in visited):
            q.append(naming(n-1,m,d+1))
            visited.append(naming(n-1,m))
    
    if m<M-1:
        if (miro[n][m+1] == '1') and (naming(n,m+1) not in visited):
            q.append(naming(n,m+1,d+1))
            visited.append(naming(n,m+1))
    
    if m>0:
        if (miro[n][m-1] == '1') and (naming(n,m-1) not in visited):
            q.append(naming(n,m-1,d+1))
            visited.append(naming(n,m-1))
    