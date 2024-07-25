N = int(input())

res = 0
a=N//10
b=N%10

while True:
    c=a+b
    a=b
    b=c%10
    res+=1
    if a*10+b==N:
        break
print(res)
