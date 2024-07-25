from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(root:list):
    q = deque()
    q.append(root)
    while q:
        now = q.popleft()
        n=now[0]
        m=now[1]
        for i in range(4):
            dn = n + dy[i]
            dm = m + dx[i]
            if 0 <= dn < N and 0 <= dm < M and array[dn][dm]==1:
                array[dn][dm] = 0
                q.append([dn,dm])

T = int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    array = [[0 for col in range(M)] for row in range(N)]
    for __ in range(K):
        m,n=map(int,input().split())
        array[n][m] = 1
    res=0
    for n in range(N):
        for m in range(M):
            if array[n][m]==1:
                bfs([n,m])
                array[n][m]=0
                res+=1
    print(res)
