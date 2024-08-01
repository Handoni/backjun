def dfs():
    check = -1
    if len(s) == M:
        print(*s)
        return
    for i in range(N):
        if check != nums[i] and not visited[i]:
            s.append(nums[i])
            visited[i] = True
            check = nums[i]
            dfs()
            s.pop()
            visited[i] = False
    
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * N
s = []
dfs()
