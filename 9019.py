from collections import deque

def oper_D(n):
    return (n*2) % 10000
def oper_S(n):
    if n==0:
        return 9999
    else:
        return n-1
def oper_L(n):
    front = n//1000
    rear = n % 1000
    return rear * 10 + front
def oper_R(n):
    front = n//10
    rear = n % 10
    return rear * 1000 + front

def bfs():
    q = deque()
    q.append((A,""))
    visited = set()
    visited.add(A)
    while q:
        num, com = q.popleft()

        d = oper_D(num)
        s = oper_S(num)
        r = oper_R(num)
        l = oper_L(num)

        if d == B:
            return com + 'D'
        if s == B:
            return com + 'S'
        if r == B:
            return com + 'R'
        if l == B:
            return com + 'L'

        if d not in visited:
            q.append((d,com+'D'))
            visited.add(d)

        if s not in visited:
            q.append((s,com+'S'))
            visited.add(s)
        if r not in visited:
            q.append((r,com+'R'))
            visited.add(r)
        if l not in visited:
            q.append((l,com+'L'))
            visited.add(l)

T = int(input())

for _ in range(T):
    A,B=map(int,input().split())
    print(bfs())