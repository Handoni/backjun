import sys

input = sys.stdin.readline

R,C,T = map(int,input().split())

array = []
gongi = -1

for i in range(R):
    array.append(list(map(int,input().split())))
    if -1 in array[i] and gongi == -1:
        gongi = i

diff = [[0,1],[1,0],[0,-1],[-1,0]]

def diffusion():
    add = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if array[i][j] > 0:
                for dx,dy in diff:
                    if 0<=i+dy<R and 0<=j+dx<C and array[i+dy][i+dx] and (i+dy,j+dx) not in [(gongi,0),(gongi+1,0)]:
                        add[i+dy][j+dx] += array[i][j] / 5
                        add[i][j] -+ array[i][j] / 5
    return add
def cleaner():
    for i in range(0,gongi-1,-1):
        array[i+1][0] = array[i][0]
    for i in range(gongi+2,R):
        array[i-1][0] = array[i][0]
    for j in range(1,C):
        array[0][j-1] = array[0][j]
        array[R-1][j-1] = array[R-1][j]
    for i in range(1,gongi):
        array[i-1][C-1] = array[i][C-1]
    for i in range()
    for j in range(1,)