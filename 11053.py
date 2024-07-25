import sys
from collections import defaultdict

input = sys.stdin.readline

A = int(input().rstrip())
nums = list(map(int, input().split()))
dp = [0 for _ in range(A)]
for i in range(A):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(max(dp))
