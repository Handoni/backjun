A, B, C = map(int, input().split(" "))

p = C-B
if p<=0:
    print("-1")
else:
    print(A//p+1)