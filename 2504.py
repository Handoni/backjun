bracket = input()
stack = []
res = 0
tmp = 1
for i in range(len(bracket)):
    if bracket[i] == '(':
        tmp *= 2
        stack.append(bracket[i])
    elif bracket[i] == '[':
        tmp *= 3
        stack.append(bracket[i])
    elif bracket[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if bracket[i-1] == '(':
            res+=tmp
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if bracket[i-1] == '[':
            res+=tmp
        tmp //=3
        stack.pop()
if stack:
    res = 0

print(res)
