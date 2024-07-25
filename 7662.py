import sys
from heapq import *
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    k = int(input().rstrip())
    q_min,q_max=[],[]
    visited = [False]*k
    
    for i in range(k):
        c,n=input().split()
        n=int(n)
        
        if c=='I':
            heappush(q_min,(n,i))
            heappush(q_max,(-n,i))
            visited[i]=True
            
        else:
            if n == 1:
                while q_max and not visited[q_max[0][1]]:
                    heappop(q_max)
                if q_max:
                    visited[q_max[0][1]] = False
                    heappop(q_max)
            else:
                while q_min and not visited[q_min[0][1]]:
                    heappop(q_min)
                if q_min:
                    visited[q_min[0][1]] = False
                    heappop(q_min)
    while q_min and not visited[q_min[0][1]]:
        heappop(q_min)
    while q_max and not visited[q_max[0][1]]:
        heappop(q_max)
        
    if not q_min or not q_max:
        print("EMPTY")
    else:
        a = -q_max[0][0]
        b = q_min[0][0]
        print(a,b)
                
        