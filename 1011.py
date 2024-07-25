t=int(input())

for _ in range(t):
    x,y =map(int,input().split(" "))
    dist = y-x
    n=1
    while dist>n**2:
        n+=1
    if dist<=(n-1)**2+(n**2-(n-1)**2)//2:
        print(n*2-2)
    else:
        print(n*2-1)