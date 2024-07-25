N = int(input())
i=0
flag=False
while N-i*3>=0:
    if (N-i*3)%5==0:
        print((N-i*3)//5+i)
        flag=True
        break
    else:
        i+=1
if not flag:
    print("-1")