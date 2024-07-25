N, M = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)
while low <= high:
    now = (low + high) // 2
    h = sum([i-now if i-now > 0 else 0 for i in trees])

    if h >= M:
        low = now + 1
    else:
        high = now - 1

print(high)