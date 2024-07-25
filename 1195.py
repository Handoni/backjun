A = input().replace('1', '0').replace('2', '1')
B = input().replace('1', '0').replace('2', '1')
len_A = len(A)
len_B = len(B)

ans = len_A + len_B
A = int(A, 2)
B = int(B, 2)

A <<= len_B
for i in range(1, len_B + 1):
    A >>= 1
    if A & B == 0:
        ans = min(ans, max(len_A + len_B - i, len_B))

B <<= len_A
for i in range(1, len_A + 1):
    B >>= 1
    if A & B == 0:
        ans = min(ans, max(len_A + len_B - i, len_A))

print(ans)