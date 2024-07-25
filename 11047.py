import sys

input = sys.stdin.readline

N,K=map(int,input().split())

A = [int(input().rstrip()) for _ in range(N)]
A = A[::-1]
cnt = 0
for i in A:
    if i<=K:
        while i<=K:
            K-=i
            cnt += 1
    if K==0:
        break
print(cnt)