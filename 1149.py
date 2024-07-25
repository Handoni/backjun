N=int(input())

cost = []
for i in range(N):
    cost.append(list(map(int, input().split(" "))))
res = []
res.append(cost[0])
for i in range(1,N):
    res.append([cost[i][0] + min(res[i-1][1],res[i-1][2]), cost[i][1] + min(res[i-1][0],res[i-1][2]), cost[i][2] + min(res[i-1][0],res[i-1][1])])
print(min(res[N-1]))