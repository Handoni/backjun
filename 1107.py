import math
import sys
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())

if M:
    array = list(input().split())
else:
    array = []

res = abs(N-100)
m=1000000
for i in range(1000000):
    flag=False
    
    for j in array:
        if j in str(i):
            flag=True
            break
    if flag:
        continue    
    m = min(m, len(str(i))+abs(N-i))
res = min(res,m)
print(res)