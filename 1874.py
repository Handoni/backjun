n = int(input())
answer = []
stack = []
now = 1

for _ in range(n):
    num = int(input())
    while now<=num:
        stack.append(now)
        answer.append("+")
        now+=1
        
    if stack[-1]==num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit()
for i in answer:
    print(i)