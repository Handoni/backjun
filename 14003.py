from bisect import bisect_left
from collections import deque
N = int(input())
A = list(map(int,input().split()))

lis = []
index = []

for num in A:
    i = bisect_left(lis, num)
    try:
        lis[i] = num
    except:
        lis.append(num)
    index.append(i)
l = len(lis)
print(l)
l -= 1

for i in range(N):
    if index[i] == l:
        m = i
        
res = deque()
while l >= 0:
    if index[m] == l:
        res.appendleft(A[m])
        l -= 1
    m -= 1
print(*res)