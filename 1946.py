T = int(input())

for _ in range(T):
    N = int(input())
    G = sorted([list(map(int,input().split())) for _ in range(N)])
    result = 1
    top = G[0][1]
    for _,m in G:
        if m < top:
            top=m
            result += 1
    print(result)