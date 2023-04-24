import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000) # 파이썬의 recursionlimit가 더 늘려줌 / 그렇지 않으면 백준에서 recursionerror 발생

n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    for i in graph[v]:
        if parents[i] == 0:
            parents[i] = v
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parents[i])