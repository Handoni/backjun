import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())

h = []
for _ in range(N):
    x = int(input().rstrip())
    if x:
        heapq.heappush(h,(-x,x))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print("0")