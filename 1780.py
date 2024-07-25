import sys
input = sys.stdin.readline

N = int(input().rstrip())

array = [list(map(int,input().split())) for _ in range(N)]

res = [0,0,0]
def func(n : int, y,x):
    num = array[y][x]
    flag=False
    for i in range(y,y+n):
        for j in range(x,x+n):
            if array[i][j] != num:
                flag=True
                for k in range(3):
                    for l in range(3):
                        func(n//3,y+k*(n//3),x+l*(n//3))
                return
    if not flag:
        res[num+1]+=1   

func(N,0,0)
for i in range(3):
    print(res[i])