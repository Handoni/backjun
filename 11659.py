import sys
input = sys.stdin.readline

N,M=map(int,input().split())
array=list(map(int,input().split()))
s=[array[0]]

for i in array[1:]:
    s.append(i+s[-1])
for _ in range(M):
    i,j=map(int,input().split())
    if i==1:
        print(s[j-1])
    else:
        print(s[j-1]-s[i-2])
    