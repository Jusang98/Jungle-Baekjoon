import sys

N, M = map(int, sys.stdin.readline().split())

matrix = [[0] * (N + 1) for _ in range(N + 1)]
visit = [False] * (N + 1)
count = 0
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    matrix[u][v] = matrix[v][u] = 1


def dfs(x):
    visit[x] = True
    for i in range(1, N + 1):
        if visit[i] == 0 and matrix[x][i] == 1:
            dfs(i)


for j in range(1, N + 1):
    if not visit[j]:
        dfs(j)
        count += 1

print(count)
