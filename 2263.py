import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input().rstrip())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i


def get_order(i_s, i_e, p_s, p_e):
    if i_s > i_e or p_s > p_e:
        return
    root = postorder[p_e]
    print(root, end=' ')

    left = position[root] - i_s
    right = i_e - position[root]
    get_order(i_s, i_s+left-1, p_s, p_s + left - 1)
    get_order(i_e-right+1, i_e, p_e-right, p_e-1)


get_order(0, n-1, 0, n-1)
