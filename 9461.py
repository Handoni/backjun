import sys
input = sys.stdin.readline

T = int(input().rstrip())
dp = dict()
dp[1]=1
dp[2]=1
dp[3]=1
for _ in range(T):
    n = int(input().rstrip())
    for i in range(4,n+1):
        if i in dp:
            continue
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])