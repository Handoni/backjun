import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())
heap=[]
for _ in range(N):
    temp=int(input().rstrip())
    if temp==0:
        try:
            print(heapq.heappop(heap))
        except IndexError:
            print("0")
    else:
        heapq.heappush(heap,temp)