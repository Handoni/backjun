strn = list(input())

stack = []
res = ""
for c in strn:
    if c.isalpha():
        res += c
    else:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack:
                temp = stack.pop()
                if temp == '(':
                    break
                else:
                    res += temp
        elif c in ['*', '/']:
            while stack:
                temp = stack.pop()
                if temp in ['*', '/']:
                    res += temp
                else:
                    stack.append(temp)
                    break
            stack.append(c)
        elif c in ['+', '-']:
            while stack:
                temp = stack.pop()
                if temp in ['*', '/', '+', '-']:
                    res += temp
                else:
                    stack.append(temp)
                    break
            stack.append(c)
while stack:
    res += stack.pop()
print(res)
