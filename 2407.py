n,m=map(int,input().split())
if m>n/2:
    m=n-m
res=1
for i in range(0,m):
    res*=n-i
for i in range(1,m+1):
    res//=i
print(res)