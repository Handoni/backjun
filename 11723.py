import sys
input = sys.stdin.readline

M=int(input().rstrip())
s=set()
for _ in range(M):
    c=input().rstrip()
    if c=="all":
        for i in range(1,21):
            s.add(i)
    elif c=="empty":
        s=set()
    else:
        c,x=c.split()
        x=int(x)
        if c=="add":
            s.add(x)
        elif c=="remove":
            try:
                s.remove(x)
            except:
                pass
        elif c=="check":
            if x in s:
                print(1)
            else:
                print(0)
        elif c=="toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)