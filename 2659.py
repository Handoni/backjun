def clockNum(a):
    min = a
    for _ in range(3):
        temp = a % 10
        a //= 10
        a += temp * 1000
        if min>a:
            min=a
    return min


a1, a2, a3, a4 = map(int,input().split(" "))
a = 1000*a1 + 100*a2 + 10*a3 + a4

clock = clockNum(a)
res = 0
for i in range(1111,clock+1):
    flag = 0
    if i != clockNum(i):
        flag = 1
    if str(i).count("0") != 0:
        flag = 1
    if flag != 1:
        res+=1

print(res)