import sys
input = sys.stdin.readline

dogam = dict()
N, M = map(int, input().split())

for i in range(1, N+1):
    t = input().rstrip()
    dogam[i] = t
    dogam[t] = i
for i in range(M):

    t = input().rstrip()
    if t.isdigit():
        print(dogam[int(t)])
    else:
        print(dogam[t])
