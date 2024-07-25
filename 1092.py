N = int(input())
W_limit = sorted(list(map(int, input().split())),reverse=True)
M = input()
W_box = sorted(list(map(int, input().split())), reverse=True)

time = 0
while(W_box):
    time += 1
    flag = False
    if W_limit[0] < W_box[0]:
        time = -1
        break
    for crain in W_limit:
        for box in W_box:
            if box <= crain:
                W_box.remove(box)
                break

print(time)