

import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N + 1)]
distance = [0] * (N + 1) # 거리 체크용
visit = [False] * (N + 1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    tree[A].append(B)



def bfs(x, k):
    res = [] # 출력용
    queue = deque([x])
    visit[x] = True
    while queue:
        x = queue.popleft()
        for i in tree[x]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True
                distance[i] = distance[x] + 1
                if distance[i] == k:
                    res.append(i)
    if len(res) == 0:
        print(-1)
    else:
        res.sort()
        for i in range(len(res)):
            print(res[i])

bfs(X, K)

