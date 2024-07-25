import sys
from collections import deque
T = int(input().rstrip())

for _ in range(T):
    p = input().rstrip()
    n = int(input().rstrip())
    array = input().rstrip()
    if array == "[]":
        array=deque()
    else:
        array = deque(map(str,array[1:-1].split(',')))
    flag=False
    rev = False
    for f in p:
        if f=='R':
            rev = not rev
        elif f=='D':
            if array:
                if rev:
                    array.pop()
                else:
                    array.popleft()
            else:
                print("error")
                flag=True
                break
    if not flag:
        print('[',end='')
        if rev:
            print(','.join(list(array)[::-1]),end='')
        else:
            print(','.join(list(array)),end='')
        print(']')