N = int(input())
if N == 1:
    print(1)
    exit()

row = [-1]*(N-1)
cnt = 0


def check(start):
    global cnt
    for num in range(N):
        flag = False
        for pre_rown in range(start):
            if (row[pre_rown] == num or abs(pre_rown-start) == abs(row[pre_rown]-num)):
                flag = True
                break
        if not flag:
            if start == N-1:
                cnt += 1
                return
            else:
                row[start] = num
                check(start+1)


for i in range(N):
    row[0] = i
    check(1)


print(cnt)
