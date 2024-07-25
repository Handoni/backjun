import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = [list(input().rstrip()) for _ in range(N)]

dy = [0,0,1,1]
dx = [0,1,0,1]
def test(n,y,x):
    start = array[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if array[i][j] != start:
                print("(",end='')
                for di,dj in zip(dy,dx):
                    test(n//2,y+di*(n//2),x+dj*(n//2))
                print(")",end='')
                return
    print(start,end="")
test(N,0,0)