import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

l1 = len(s1)
l2 = len(s2)

dp = [[0]*(l1+1) for _ in range(l2+1)]

for i in range(l2):
    for j in range(l1):
        if s1[j] == s2[i]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[l2][l1])
