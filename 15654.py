from itertools import permutations

N,M=map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
p = list(permutations(nums,M))
p.sort()
for c in p:
    for i in c:
        print(i,end=' ')
    print()