T = int(input())

for _ in range(T):
    N = int(input())

    p_2 = [1,0]
    p_1 = [0,1] 

    if N == 0:
        print("1 0")
    elif N == 1:
        print("0 1")
    else:
        for i in range(2,N+1):
            temp = [p_2[0]+p_1[0],p_2[1]+p_1[1]]
            p_2=p_1[:]
            p_1=temp[:]
        print(str(p_1[0])+' '+str(p_1[1]))
        