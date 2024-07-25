import sys
input = sys.stdin.readline

N = int(input().rstrip())

array = list()
for i in range(N):
    array.append(list(map(int, input().split())))

white,blue=0,0
def test(x,y,n):
    global white,blue
    t = array[y][x]
    flag = False
    for i in range(n):
        for j in range(n):
            if array[y+i][x+j] != t:
                flag = True
                test(x,y,n//2)
                test(x+n//2,y,n//2)
                test(x,y+n//2,n//2)
                test(x+n//2,y+n//2,n//2)
                return
    if not flag:
        if t==0:
            white+=1
        else :
            blue+=1
test(0,0,N)
print(white)
print(blue)

    
            
