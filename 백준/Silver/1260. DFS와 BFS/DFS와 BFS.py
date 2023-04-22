import sys

# N은 정점의 개수 M은 간선의 개수, V는 탐색을 시작할 정점의 번호
N, M, V = map(int, sys.stdin.readline().split())

matrix = [[0] * (N + 1) for _ in range(N + 1)]  # 인접영 행렬
visit = [0] * (N + 1)  # 방문 체크 행렬

# 입력 받는 두값에 대해 영행렬에 1 삽입
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1


def dfs(v):
    visit[v] = 1
    print(v, end=" ")
    for i in range(1, N + 1): # 방문 안한애들만
        if visit[i] == 0 and matrix[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 0 # 1로 바뀐 visit들을 0으로
    while queue: # 큐안에 데이터 다 없어질때까지 돌려
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1, N + 1):
            if visit[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visit[i] = 0


dfs(V)
print()
bfs(V)
