N = int(input())

array = list(map(int,input().split()))

array = sorted(array)
res=0
for i in range(N):
    res+=array[i]*(N-i)
print(res)