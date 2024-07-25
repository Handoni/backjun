import sys
input = sys.stdin.readline

N = int(input().rstrip())

array = list(map(int, input().split()))

arr2 = sorted(list(set(array)))
dic = {arr2[i]: i for i in range(len(arr2))}

for i in array:
    print(dic[i], end=' ')
