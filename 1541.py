from itertools import combinations

s = input()

pos1=0
pos2=0
num = []
while True:
    pos2+=1
    if pos2 == len(s):
        num.append(sum(map(int,s[pos1:pos2].split('+'))))
        break
    if s[pos2] == '-':
        num.append(sum(map(int,s[pos1:pos2].split('+'))))
        pos1=pos2+1

res=num[0]
for i in num[1:]:
    res-=i
print(res)