A,B,C=map(int,input().split())

res=1

while B:
    if B%2 != 0:
        res*=A%C
    A=(A%C)**2
    B//=2

print(res%C)