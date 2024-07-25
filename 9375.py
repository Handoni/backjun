import sys
from collections import defaultdict

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    d = defaultdict(lambda:[])
    for __ in range(n):
        value,key = input().split()
        d[key].append(value)
    
    l = list(d.values())
    res=1
    for i in l:
        res*=len(i)+1
    print(res-1)