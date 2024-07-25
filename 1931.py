import sys
input = sys.stdin.readline

N = int(input().rstrip())
tlist=list()

for _ in range(N):
    tlist.append(list(map(int,input().split())))
tlist.sort(key=lambda x: x[0])
tlist.sort(key=lambda x:x[1])

cnt=1
end=tlist[0][1]
for i in range(1,N):
    if end<=tlist[i][0]:
        cnt+=1
        end=tlist[i][1]
print(cnt)