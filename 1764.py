import sys
input = sys.stdin.readline

N,M=map(int,input().split())

d = set()
b = set()
for _ in range(N):
    d.add(input().rstrip())
for _ in range(M):
    b.add(input().rstrip())
a = list(d&b)
print(len(a))
for i in sorted(a):
    print(i)