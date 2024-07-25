from collections import deque

N ,M = map(int,input().split(" "))
q = deque()
q.extend(list(map(lambda x: x, range(1, N+1))))

num = list(map(int,input().split(" ")))
res=0
for i in num:
    temp = list(q)
    for j in range(N):
        if temp[j] == i:
            if j<=N/2:
                q.rotate(-(j))
                res+=j
            else:
                q.rotate(N-j)
                res+=N-j
            q.popleft()
            M-=1
            N-=1
            break
print(res)