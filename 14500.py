import sys
input = sys.stdin.readline

N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
diff = [[0,1],[1,0],[0,-1],[-1,0]]
res = -1

def dfs(x,y,dsum,cnt):
    global res
    if cnt == 4:
        res = max(res,dsum)
        return
    for dx,dy in diff:
        nx,ny = x+dx,y+dy
        if 0<=nx<M and 0<=ny<N and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx,ny,dsum+graph[ny][nx],cnt+1)
            visited[ny][nx] = False
def yut(x,y):
    global res
    for i in range(4):
        temp = graph[y][x]
        for j in range(3):
            t = (i+j)%4
            dx,dy = diff[t]
            nx,ny = x+dx,y+dy
            if not (0<=nx<M and 0<=ny<N):
                temp = 0
                break
            temp += graph[ny][nx]
        res = max(res,temp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(j,i,graph[i][j],1)
        visited[i][j] = False
        yut(j,i)
print(res)