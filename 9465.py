import sys

input = sys.stdin.readline

T = int(input().rstrip())
for ____ in range(T):
    n = int(input().rstrip())
    array = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(array[0][0], array[1][0]))
    else:
        dp = [[0 for _ in range(n)] for __ in range(2)]
        dp[0][0], dp[1][0] = array[0][0], array[1][0]
        dp[0][1], dp[1][1] = dp[1][0]+array[0][1], dp[0][0]+array[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + array[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + array[1][i]
        print(max(dp[0][-1], dp[1][-1]))
