dp=dict()

dp[1] = 1
dp[2] = 2

n = int(input())
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)