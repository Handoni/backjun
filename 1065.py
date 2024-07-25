N = int(input())
res=0
for i in range(1,N+1):
    digit=i%10
    i//=10
    if i==0:
        res+=1
        continue
    
    diff=i%10-digit
    digit=i%10
    i//=10
    
    flag=False
    while i>0:
        if i%10 - digit != diff:
            flag=True
            break
        else:
            digit=i%10
            i//=10
    if not flag:
        res+=1
print(res)