N=int(input())

res=0
fac=1
for i in range(1,N+1):
    fac *= i
    while True:
        a = fac%10
        if a == 0:
            res+=1
            fac//=10
        else:
            break
print(res)
    