import sys
sys.setrecursionlimit(10000)

N = int(input())
P = 1000000007

nums = dict()
nums[0] = 0
nums[1] = 1


def fibo(num):
    if not num in nums:
        if num % 2 == 0:
            fn = fibo(num//2)
            fnP1 = fibo(num//2 + 1)
            nums[num] = (fn * ((2*fnP1-fn))) % P
        else:
            fnP1 = fibo(num//2 + 1)
            fn = fibo(num//2)
            nums[num] = (fnP1*fnP1 + fn*fn) % P
    return nums[num]


print(fibo(N))
