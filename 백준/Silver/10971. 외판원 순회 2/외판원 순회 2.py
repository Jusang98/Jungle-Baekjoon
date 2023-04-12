import sys
input = sys.stdin.readline
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
visited = [0]* n
sum_cost = 0
ans = sys.maxsize
def dfs(depth, x):
    global sum_cost, ans
    if depth == n-1:
        if costs[x][0]:
            sum_cost += costs[x][0]
            if sum_cost < ans:
                ans = sum_cost
            sum_cost -= costs[x][0]
        return
    for i in range(1, n):
        if visited[i] == 0 and costs[x][i]:
            visited[i] = 1
            sum_cost += costs[x][i]
            dfs(depth+1, i)
            visited[i] = 0
            sum_cost -= costs[x][i]
dfs(0, 0)
print(ans)