import sys

input = sys.stdin.readline

n = int(input().rstrip())

tri= [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*i for i in range(1,n+1)]
dp[0][0] = tri[0][0]

for i in range(n-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i+1][j], tri[i+1][j] + dp[i][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], tri[i+1][j+1] + dp[i][j])
print(max(dp[n-1]))