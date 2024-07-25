from itertools import combinations

N,M=map(int,input().split())
nums = [i for i in range(1,N+1)]
combi = list(combinations(nums,M))
combi.sort()
for i in combi:
    for j in i:
        print(j,end=' ')
    print()