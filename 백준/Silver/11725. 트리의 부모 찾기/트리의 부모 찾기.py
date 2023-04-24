import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):  # 간선의 갯수 = 노드 개수 - 1
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(v):
    for i in tree[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)


dfs(1)

for j in range(2, len(parent)):
    print(parent[j])
