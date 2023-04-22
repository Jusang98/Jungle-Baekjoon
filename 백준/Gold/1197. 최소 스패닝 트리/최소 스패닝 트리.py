import sys


def find(parent, x):  # 부모노드 비교
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):  # 합치면서 부모노드가 더 작은쪽으로 부모를 바꿔
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, sys.stdin.readline().split())  # V는 정점 개수, E는 간선갯수
parents = [0] * (V + 1) # 부모 노드 초기화
for i in range(1, V + 1):
    parents[i] = i

edges = []  # 간선 정보
total = 0  # 총 가중치의 합
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((C, A, B))
edges.sort() # 가중치 오름차순으로 정렬

for i in range(E):
    C, A, B = edges[i]
    if find(parents, A) != find(parents, B): # 부모노드가 다를시엔 사이클연산 발생하지않음! union 함수 실행 -> 가중치 합
        union(parents, A, B)
        total += C

print(total)
