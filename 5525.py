import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

i = 1
cnt = 0
ans = 0
while i < M-1:
    if S[i] == 'O' and S[i-1] == 'I' and S[i+1] == 'I':
        cnt += 1
        if cnt == N:
            cnt-=1
            ans+=1
        i+=1
    else:
        cnt=0
    i+=1
print(ans)