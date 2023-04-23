import sys

N = int(sys.stdin.readline())  # N은 컴퓨터의 개수
M = int(sys.stdin.readline())  # M은 간선의 개수

matrix = [[0] * (N + 1) for _ in range(N + 1)]  # 영행렬
virus = [0] * (N + 1)
count = 0
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1


def dfs(v):
    global count
    virus[v] = 1
    for i in range(1, N + 1):
        if virus[i] == 0 and matrix[v][i] == 1:
            count += 1
            dfs(i)


dfs(1)

print(count) # 처음 감염된 컴퓨터는 카운팅 x
