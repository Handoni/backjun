import sys
inf = sys.maxsize
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
array = [[inf]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    array[a-1][b-1] = min(array[a-1][b-1], c)

for i in range(n):
    for j in range(n):
        if i == j:
            array[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            array[i][j] = min(array[i][j], array[i][k] + array[k][j])


for l in array:
    for c in l:
        if c == inf:
            print(0, end=' ')
        else:
            print(c, end=' ')
    print()
