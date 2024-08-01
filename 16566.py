import sys
input = sys.stdin.readline

def find(n):
    if reps[n] != n:
        reps[n] = find(reps[n])
    return reps[n]

def union(x, y):
    x = find(x)
    y = find(y)
    reps[x] = y

N, M, K = map(int, input().split())
nums = sorted(list(map(int, input().split())))
seq = list(map(int, input().split()))
reps = [i for i in range(M + 1)]

for i in seq:
    left = 0
    right = len(nums) - 1
    while(left < right):
        mid = (left + right) // 2
        if nums[mid] <= i:
            left = mid + 1
        else:
            right = mid
    index = find(right)
    print(nums[index])
    union(index, index + 1)