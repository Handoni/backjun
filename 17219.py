import sys
input = sys.stdin.readline

N,M = map(int,input().split())

saved = dict()
for _ in range(N):
    key,value = input().split()
    saved[key]=value
for _ in range(M):
    k = input().rstrip()
    print(saved[k])